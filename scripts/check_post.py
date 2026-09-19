#!/usr/bin/env python3
# ==============================================================================
# File: check_post.py
# Description: Checks a generated post for the faults a converter leaves behind:
#   LaTeX that never got translated, cross-references that resolved to nothing,
#   citations pointing at absent anchors, unbalanced markup, and figures whose
#   image files are missing. Exits non-zero on any of them.
# Usage: py scripts/check_post.py <path to index.md>
# Author: Amey Thakur
# License: CC-BY-4.0
# ==============================================================================

import pathlib
import re
import sys
from collections import Counter

SAFE_BACKSLASH = re.compile(r"\\[\\`*_{}\[\]()#+\-.!|]")   # markdown escapes


def main(path_str: str) -> int:
    path = pathlib.Path(path_str)
    text = path.read_text(encoding="utf-8")
    body = text.split("---", 2)[2] if text.startswith("---") else text
    fails, notes = [], []

    def check(ok, msg):
        (notes if ok else fails).append(msg)

    # --- LaTeX that survived ------------------------------------------------
    # Not just \word: a spacing escape like the thin space in "53\,ms" is
    # equally untranslated and equally visible on the page.
    leftovers = Counter()
    for m in re.finditer(r"\\[a-zA-Z]+|\\[,;:!&%#_ ]", body):
        if SAFE_BACKSLASH.fullmatch(m.group(0)):
            continue
        leftovers[m.group(0)] += 1
    check(not leftovers,
          f"untranslated LaTeX: {dict(leftovers.most_common(8))}")

    stray_bs = body.count("\\") - sum(leftovers.values())
    check(stray_bs == 0, f"other stray backslashes: {stray_bs}")

    for token in ("\\begin{", "\\end{", "&amp;", "\\item", "$"):
        n = body.count(token)
        check(n == 0, f"stray {token!r}: {n}")

    # --- cross-references ---------------------------------------------------
    unresolved = len(re.findall(r"(?:Section|Table|Figure|Proposition|Corollary|"
                                r"Definition|Equation)~?\s*\?", body))
    check(unresolved == 0, f"cross-references that resolved to '?': {unresolved}")

    # --- citations point at anchors that exist ------------------------------
    cited = {int(n) for n in re.findall(r"\[\[(\d+)\]\]\(#ref-\d+\)", body)}
    anchors = {int(n) for n in re.findall(r'<a id="ref-(\d+)">', body)}
    check(not (cited - anchors), f"citations with no anchor: {sorted(cited - anchors)}")
    check(not (anchors - cited), f"references never cited: {sorted(anchors - cited)}")
    notes.append(f"references: {len(anchors)}, distinct cited: {len(cited)}")

    # --- images exist -------------------------------------------------------
    missing = [src for src in re.findall(r'Academic_Figure src="([^"]+)"', body)
               if not (path.parent / src).is_file()]
    check(not missing, f"figure files missing: {missing}")
    notes.append(f"figures: {len(re.findall(r'Academic_Figure', body))}")

    # --- markup balance -----------------------------------------------------
    for tag in ("i", "sub", "sup", "b", "span", "code", "pre", "div"):
        o = len(re.findall(rf"<{tag}[ >]", body))
        c = len(re.findall(rf"</{tag}>", body))
        check(o == c, f"<{tag}> opened {o} times, closed {c}")

    # --- structure ----------------------------------------------------------
    for needed in ("## Abstract", "## Citation", "## References"):
        check(needed in body, f"missing section: {needed}")
    notes.append(f"headings: {len(re.findall(r'(?m)^## ', body))} h2, "
                 f"{len(re.findall(r'(?m)^### ', body))} h3")
    # an alignment row marks one rendered table; the pipe must be escaped or
    # the regex reads it as alternation and counts every horizontal rule too
    notes.append(f"table blocks: {len(re.findall(r'(?m)^\|[-: |]+\|$', body))}")
    notes.append(f"words: {len(body.split()):,}")

    # --- front matter -------------------------------------------------------
    fm = text.split("---")[1] if text.startswith("---") else ""
    for key in ("title:", "date:", "author:", "summary:", "tags:", "ShowToc:"):
        check(key in fm, f"front matter missing {key}")

    for n in notes:
        print(f"  ok    {n}")
    for f in fails:
        print(f"  FAIL  {f}")
    print(f"\n{len(notes)} passed, {len(fails)} failed")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
