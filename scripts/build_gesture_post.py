#!/usr/bin/env python3
# ==============================================================================
# File: build_gesture_post.py
# Description: Builds the Amey's Arc post for the GESTURE-FX paper from its
#   arXiv source, word for word, so the post and the announced manuscript
#   cannot drift apart. Re-run it whenever main.tex changes.
#
#   This paper uses BibTeX, so its rendered bibliography lives in main.bbl
#   rather than inside the manuscript, and the builder is pointed at it.
#
# Usage: py scripts/build_gesture_post.py
# Author: Amey Thakur
# License: CC-BY-4.0
# ==============================================================================

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import paper_to_post as P

SITE = pathlib.Path(__file__).resolve().parents[1]
SRC = pathlib.Path(
    r"C:\Users\archi\AppData\Local\Temp\claude"
    r"\C--Users-archi-OneDrive-Desktop-Shreyas"
    r"\dfd771df-6c1c-415b-9cd4-f4a3bfa0bf03\scratchpad\gesture")
SLUG = "2026-08-31-frame-synchronous-hand-gesture-detection-by-projected-winding-order"
OUT = SITE / "content" / "posts" / SLUG

TITLE = "Frame-Synchronous Hand Gesture Detection by Projected Winding Order"

TAGS = ["Computer Vision", "Gesture Recognition", "Hand Tracking",
        "Real-Time Systems", "WebGL", "Browser", "Non-Photorealistic Rendering",
        "Projective Geometry", "MediaPipe", "Human-Computer Interaction",
        "TypeScript", "On-Device Inference", "Signal Processing"]

# figure label -> the image the post shows
FIGDIR = {
    "fig:geometry": "geometry.png",
    "fig:pipeline": "fig-2-pipeline.png",
    "fig:rewind": "rewind_cut.jpg",
}

LINKS = (
    "**[arXiv:2609.13269](https://arxiv.org/abs/2609.13269)** &nbsp;·&nbsp;\n"
    "**[Code](https://github.com/Amey-Thakur/GESTURE-FX)** &nbsp;·&nbsp;\n"
    "**[Live demo](https://amey-thakur.github.io/GESTURE-FX/)**"
)

HEADER_NOTE = (
    "> This is the paper in full, as announced on arXiv as "
    "**[arXiv:2609.13269](https://arxiv.org/abs/2609.13269)**. The code that "
    "produced every figure, and a demo that runs in the browser, are at "
    "**[Amey-Thakur/GESTURE-FX](https://github.com/Amey-Thakur/GESTURE-FX)**."
)

CITATION = ('Thakur, Amey. "Frame-Synchronous Hand Gesture Detection by '
            'Projected Winding Order." arXiv:2609.13269 (Sep 2026). '
            'https://arxiv.org/abs/2609.13269.')

BIBTEX = """@article{thakur2026winding,
  title         = "Frame-Synchronous Hand Gesture Detection by Projected Winding Order",
  author        = "Thakur, Amey",
  journal       = "arXiv preprint arXiv:2609.13269",
  year          = "2026",
  month         = "Sep",
  eprint        = "2609.13269",
  archivePrefix = "arXiv",
  url           = "https://arxiv.org/abs/2609.13269"
}"""


def summary_from_abstract(tex_path, sentences=4):
    """The opening of the paper's own abstract, so the teaser is its words."""
    tex = pathlib.Path(tex_path).read_text(encoding="utf-8")
    abstract = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", tex, re.S).group(1)
    plain = P.clean_text(re.sub(r"\s+", " ", abstract))
    plain = re.sub(r"<[^>]+>|&[a-zA-Z#0-9]+;", "", plain)
    parts = re.split(r"(?<=\.)\s+", plain.strip())
    return " ".join(parts[:sentences]).replace('"', "'").strip()


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    text = P.build(
        tex_path=SRC / "main.tex",
        bbl_path=SRC / "main.bbl",
        out_path=OUT / "index.md",
        title=TITLE,
        date="2026-08-31T21:40:12-04:00",
        summary=summary_from_abstract(SRC / "main.tex"),
        tags=TAGS,
        card="social_preview.png",
        links=LINKS,
        header_note=HEADER_NOTE,
        figdir=FIGDIR,
        accessed="Sep. 20, 2026",
        citation_text=CITATION,
        bibtex=BIBTEX,
    )
    print(f"wrote {OUT / 'index.md'}: {len(text.splitlines())} lines, "
          f"{len(text.split())} words")


if __name__ == "__main__":
    main()
