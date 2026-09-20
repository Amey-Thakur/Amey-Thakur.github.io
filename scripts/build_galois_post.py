#!/usr/bin/env python3
# ==============================================================================
# File: build_galois_post.py
# Description: Builds the Amey's Arc post for the Chebotarev Fingerprints paper
#   from its arXiv source, so the post and the manuscript cannot drift apart.
#   Re-run it whenever main.tex changes.
#
#   The arXiv line is deliberately absent from the header: the paper has not
#   been announced yet, and a link that does not resolve is worse than no link.
#   Add it here once the identifier exists.
#
# Usage: py scripts/build_galois_post.py
# Author: Amey Thakur
# License: CC-BY-4.0
# ==============================================================================

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import paper_to_post as P

SITE = pathlib.Path(__file__).resolve().parents[1]
TEX = SITE.parent / "SAIR-INVERSE-GALOIS-ARXIV" / "main.tex"
SLUG = "2026-09-20-chebotarev-fingerprints-identifying-degree-24-galois-groups"
OUT = SITE / "content" / "posts" / SLUG

TITLE = ("Chebotarev Fingerprints: Identifying Degree-24 Galois Groups "
         "Without Computer Algebra")

def summary_from_abstract(tex_path, sentences=4):
    """The opening of the paper's own abstract.

    The summary is the one line a reader sees before opening the post, so it
    should be the paper's words rather than a gloss written around them.
    """
    import re
    tex = pathlib.Path(tex_path).read_text(encoding="utf-8")
    abstract = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", tex, re.S).group(1)
    plain = P.clean_text(re.sub(r"\s+", " ", abstract))
    plain = re.sub(r"<[^>]+>|&[a-zA-Z#0-9]+;", "", plain)
    parts = re.split(r"(?<=\.)\s+", plain.strip())
    return " ".join(parts[:sentences]).replace('"', "'").strip()

TAGS = ["Mathematics", "Number Theory", "Galois Theory", "Chebotarev Density",
        "Inverse Galois Problem", "Transitive Groups", "Statistical Classification",
        "Computational Mathematics", "LMFDB", "SAIR Foundation", "Research",
        "Python", "Machine Learning"]

# figure label -> the image cropped out of the compiled PDF
FIGDIR = {
    "fig:idea": "fig-1-method-without-notation.png",
    "fig:pipeline": "fig-2-classifier-pipeline.png",
    "fig:bound": "fig-3-separability-bound.png",
    "fig:crowding": "fig-4-crowding-distribution.png",
    "fig:ablation": "fig-5-accuracy-vs-primes.png",
}

LINKS = (
    "**[Code and data](https://github.com/Amey-Thakur/SAIR-INVERSE-GALOIS-PROBLEM-IGP24)** &nbsp;·&nbsp;\n"
    "**[Competition](https://competition.sair.foundation/competitions/igp24/overview)** &nbsp;·&nbsp;\n"
    "**[SAIR Foundation index](https://github.com/Amey-Thakur/SAIR-FOUNDATION-FOR-SCIENCE-AND-AI-RESEARCH)**"
)

CITATION = ('Thakur, Amey. "Chebotarev Fingerprints: Identifying Degree-24 Galois '
            'Groups Without Computer Algebra" (Sep 2026). '
            'https://github.com/Amey-Thakur/SAIR-INVERSE-GALOIS-PROBLEM-IGP24.')

BIBTEX = """@article{thakur2026chebotarev,
  title   = "Chebotarev Fingerprints: Identifying Degree-24 Galois Groups Without Computer Algebra",
  author  = "Thakur, Amey",
  year    = "2026",
  month   = "Sep",
  url     = "https://github.com/Amey-Thakur/SAIR-INVERSE-GALOIS-PROBLEM-IGP24"
}"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    text = P.build(
        tex_path=TEX,
        out_path=OUT / "index.md",
        title=TITLE,
        date="2026-09-20T09:00:00-04:00",
        summary=summary_from_abstract(TEX),
        tags=TAGS,
        card="card.gif",
        links=LINKS,
        figdir=FIGDIR,
        accessed="Sep. 20, 2026",
        citation_text=CITATION,
        bibtex=BIBTEX,
    )
    print(f"wrote {OUT / 'index.md'}: {len(text.splitlines())} lines, "
          f"{len(text.split())} words")


if __name__ == "__main__":
    main()
