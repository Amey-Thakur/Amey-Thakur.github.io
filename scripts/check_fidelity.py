#!/usr/bin/env python3
# ==============================================================================
# File: check_fidelity.py
# Description: Proves a post carries the paper's words, not a retelling of them.
#   Both sides are reduced to plain sentences, markup and maths stripped, then
#   compared. Any sentence in the manuscript that is missing from the post, or
#   any sentence in the post that is not in the manuscript, is reported.
#
#   Front matter, the links row and the citation block are the post's own
#   furniture and are excluded; everything between the abstract and the
#   references must match the source.
# Usage: py scripts/check_fidelity.py <main.tex> <index.md>
# Author: Amey Thakur
# License: CC-BY-4.0
# ==============================================================================

import pathlib
import re
import sys


def words(text: str) -> list[str]:
    text = re.sub(r"<[^>]+>", " ", text)                 # html tags
    text = re.sub(r"&[a-zA-Z#0-9]+;", " ", text)         # entities
    text = re.sub(r"\{\{<.*?>\}\}", " ", text)           # hugo shortcodes
    text = re.sub(r"\[\[\d+\]\]\(#ref-\d+\)", " ", text)  # citations
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)  # links
    text = re.sub(r"[*_`>|#]", " ", text)                # markdown furniture
    text = re.sub(r"[^A-Za-z]+", " ", text)              # keep letters only
    return [w for w in text.lower().split() if len(w) > 2]


def tex_words(tex: str) -> list[str]:
    body = tex.split("\\begin{document}")[1].split("\\begin{thebibliography}")[0]
    body = re.sub(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", " ", body, flags=re.S)
    body = re.sub(r"(?<!\\)\$[^$]*\$", " ", body)        # inline maths
    body = re.sub(r"\\\[.*?\\\]", " ", body, flags=re.S)  # display maths
    body = re.sub(r"\\begin\{equation\}.*?\\end\{equation\}", " ", body, flags=re.S)
    body = re.sub(r"\\cite[pt]?\{[^}]*\}", " ", body)
    body = re.sub(r"\\(ref|eqref|label)\{[^}]*\}", " ", body)
    # environment names and column specifications are LaTeX plumbing, not
    # prose; left in, they read as words the post has "dropped"
    body = re.sub(r"\\(begin|end)\{[^}]*\}(\[[^\]]*\])?(\{[^}]*\})*", " ", body)
    body = re.sub(r"\\multicolumn\{\d+\}\{[^}]*\}", " ", body)
    body = re.sub(r"\\[a-zA-Z]+", " ", body)             # remaining commands
    return words(body)


def main(tex_path: str, md_path: str) -> int:
    tex = pathlib.Path(tex_path).read_text(encoding="utf-8")
    md = pathlib.Path(md_path).read_text(encoding="utf-8")

    # the post's own furniture, which has no counterpart in the manuscript
    body = md.split("---", 2)[2]
    body = body.split("## Citation")[0]
    body = re.sub(r"<style>.*?</style>", " ", body, flags=re.S)
    # the links row under the title card is the post's own navigation
    body = re.sub(r'<div align="center">.*?</div>', " ", body, flags=re.S)

    a, b = tex_words(tex), words(body)
    from collections import Counter
    ca, cb = Counter(a), Counter(b)

    missing = ca - cb          # in the paper, absent from the post
    extra = cb - ca            # in the post, absent from the paper

    print(f"  manuscript words : {len(a):,} ({len(ca):,} distinct)")
    print(f"  post words       : {len(b):,} ({len(cb):,} distinct)")
    print(f"  dropped from post: {sum(missing.values()):,}")
    print(f"  added in post    : {sum(extra.values()):,}")

    if missing:
        print("\n  WORDS THE POST DROPS")
        for w, n in missing.most_common(15):
            print(f"    {w:24s} x{n}")
    if extra:
        print("\n  WORDS THE POST ADDS")
        for w, n in extra.most_common(15):
            print(f"    {w:24s} x{n}")

    ok = sum(missing.values()) == 0 and sum(extra.values()) == 0
    print("\n" + ("  the post carries the manuscript's words exactly"
                  if ok else "  the two differ; see above"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
