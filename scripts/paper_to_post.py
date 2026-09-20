#!/usr/bin/env python3
# ==============================================================================
# File: paper_to_post.py
# Description: Turns an arXiv manuscript into an Amey's Arc post, word for word.
#   The site carries no MathJax or KaTeX, so every formula becomes HTML
#   typography in the house `.equation` style: Unicode symbols, italic
#   variables, real sub- and superscripts. Citations become the clickable
#   [[n]](#ref-n) form the other posts use, cross-references resolve to the
#   numbers the compiled paper shows, tables become Markdown, and figures
#   become Academic_Figure shortcodes pointing at images cropped from the PDF.
#
#   The point is fidelity. Nothing is summarised, reordered or reworded; the
#   only changes are the ones the web demands.
#
# Usage: py scripts/paper_to_post.py --tex <main.tex> --out <index.md> [--no-arxiv]
# Author: Amey Thakur
# License: CC-BY-4.0
# ==============================================================================

from __future__ import annotations

import argparse
import pathlib
import re

# ---------------------------------------------------------------------------
# symbols
# ---------------------------------------------------------------------------

SYMBOLS = {
    r"\rho": "&rho;", r"\pi": "&pi;", r"\lambda": "&lambda;", r"\tau": "&tau;",
    r"\delta": "&delta;", r"\varepsilon": "&epsilon;", r"\epsilon": "&epsilon;",
    r"\Lambda": "&Lambda;", r"\Delta": "&Delta;", r"\theta": "&theta;",
    r"\alpha": "&alpha;", r"\beta": "&beta;", r"\gamma": "&gamma;",
    r"\sigma": "&sigma;", r"\mu": "&mu;", r"\ell": "<i>&#8467;</i>",
    r"\leq": "&le;", r"\geq": "&ge;", r"\neq": "&ne;", r"\approx": "&asymp;",
    r"\cdot": "&middot;", r"\times": "&times;", r"\pm": "&plusmn;",
    r"\in": "&isin;", r"\notin": "&notin;", r"\subseteq": "&sube;",
    r"\subset": "&sub;", r"\infty": "&infin;", r"\equiv": "&equiv;",
    r"\otimes": "&otimes;", r"\to": "&rarr;", r"\mapsto": "&#8614;",
    r"\ldots": "&hellip;", r"\dots": "&hellip;", r"\cdots": "&hellip;",
    r"\sum": "&Sigma;", r"\prod": "&Pi;", r"\max": "max", r"\min": "min",
    r"\log": "log", r"\exp": "exp", r"\deg": "deg", r"\arg": "arg",
    r"\bmod": "mod", r"\quad": " &nbsp; ", r"\qquad": " &nbsp;&nbsp; ",
    r"\;": " ", r"\,": "&thinsp;", r"\!": "", r"\:": " ",
    r"\tanh": "tanh", r"\cosh": "cosh", r"\sinh": "sinh",
    r"\cos": "cos", r"\sin": "sin", r"\tan": "tan", r"\atan": "atan",
    r"\star": "&#8902;", r"\kappa": "&kappa;", r"\omega": "&omega;",
    r"\Omega": "&Omega;", r"\phi": "&phi;", r"\varphi": "&phi;",
    r"\nu": "&nu;", r"\eta": "&eta;", r"\zeta": "&zeta;",
    r"\cup": "&cup;", r"\cap": "&cap;", r"\chi": "&chi;",
    r"\le": "&le;", r"\ge": "&ge;", r"\circ": "&compfn;",
    r"\sim": "&sim;", r"\propto": "&prop;", r"\partial": "&part;",
    r"\langle": "&lang;", r"\rangle": "&rang;", r"\emptyset": "&empty;",
    r"\setminus": "&#8726;", r"\forall": "&forall;", r"\exists": "&exist;",
    r"\gg": "&Gt;", r"\ll": "&Lt;", r"\iff": "&hArr;",
    r"\implies": "&rArr;", r"\perp": "&perp;", r"\angle": "&ang;",
    r"\big": "", r"\Big": "", r"\bigg": "", r"\Bigg": "",
    r"\natexlab": "", r"\hspace": "", r"\mspace": "",
    r"\left": "", r"\right": "", r"\bigl": "", r"\bigr": "",
    r"\Bigl": "", r"\Bigr": "", r"\displaystyle": "",
}

BLACKBOARD = {"Z": "&#8484;", "Q": "&#8474;", "R": "&#8477;", "N": "&#8469;",
              "C": "&#8450;", "F": "&#120125;"}
SCRIPT = {"T": "&#119983;", "P": "&#119979;", "L": "&#119974;"}


def _braced(s: str, i: int) -> tuple[str, int]:
    """Contents of the brace group starting at s[i] == '{', and the index past it."""
    assert s[i] == "{"
    depth, j = 0, i
    while j < len(s):
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    raise ValueError("unbalanced brace in math: " + s[i:i + 40])


def _take(s: str, i: int) -> tuple[str, int]:
    """One argument: a brace group, a command, or a single character."""
    if i < len(s) and s[i] == "{":
        return _braced(s, i)
    m = re.match(r"\\[a-zA-Z]+", s[i:])
    if m:
        return m.group(0), i + m.end()
    return s[i], i + 1


def math(src: str) -> str:
    """One LaTeX math expression as HTML.

    Handles the constructs this manuscript actually uses. Anything unknown is
    passed through rather than silently dropped, so a gap shows up as visible
    LaTeX in review instead of as missing content.
    """
    s = src.strip()
    out, i = [], 0
    while i < len(s):
        ch = s[i]

        if ch == "\\":
            m = re.match(r"\\[a-zA-Z]+", s[i:])
            cmd = m.group(0) if m else s[i:i + 2]

            if cmd in (r"\frac", r"\tfrac", r"\dfrac"):
                num, j = _take(s, i + len(cmd))
                den, j = _take(s, j)
                out.append(f"{_wrap(math(num))}&#8260;{_wrap(math(den))}")
                i = j
                continue
            if cmd == r"\sqrt":
                arg, j = _take(s, i + len(cmd))
                inner = math(arg)
                out.append(f"&radic;<span style=\"text-decoration:overline\">{inner}</span>")
                i = j
                continue
            if cmd in (r"\mathbb", r"\mathcal", r"\mathrm", r"\mathbf",
                       r"\operatorname", r"\text", r"\textit", r"\texttt"):
                arg, j = _take(s, i + len(cmd))
                if cmd == r"\mathbb":
                    out.append(BLACKBOARD.get(arg, arg))
                elif cmd == r"\mathcal":
                    out.append(SCRIPT.get(arg, arg))
                elif cmd == r"\texttt":
                    out.append(f"<code>{arg}</code>")
                else:
                    out.append(arg)          # upright
                i = j
                continue
            if cmd == r"\hat":
                arg, j = _take(s, i + len(cmd))
                out.append(math(arg) + "&#770;")     # combining circumflex
                i = j
                continue
            if cmd in (r"\lVert", r"\rVert", r"\|"):
                out.append("&#8214;")
                i += len(cmd)
                continue
            if cmd == r"\pmod":
                arg, j = _take(s, i + len(cmd))
                out.append(f" (mod {math(arg)})")
                i = j
                continue
            if cmd in ("\\{", "\\}"):
                out.append(cmd[1])          # a literal set brace
                i += 2
                continue
            if cmd in SYMBOLS:
                out.append(SYMBOLS[cmd])
                i += len(cmd)
                continue
            # unknown command: keep it visible
            out.append(cmd)
            i += len(cmd)
            continue

        if ch == "_" or ch == "^":
            arg, j = _take(s, i + 1)
            tag = "sub" if ch == "_" else "sup"
            out.append(f"<{tag}>{math(arg)}</{tag}>")
            i = j
            continue

        if ch == "{":
            grp, j = _braced(s, i)
            out.append(math(grp))
            i = j
            continue

        if ch.isalpha():
            # a run of letters is a variable name, set in italic; a known
            # function word is not
            m = re.match(r"[A-Za-z]+", s[i:])
            word = m.group(0)
            if word in ("mod", "max", "min", "log", "exp", "deg", "arg", "disc",
                        "Gal", "TV", "if", "and", "or", "for"):
                out.append(word)
            else:
                out.append(f"<i>{word}</i>")
            i += len(word)
            continue

        # a bare < or > in HTML output starts something the browser tries to
        # read as a tag, so comparison operators are escaped
        out.append({"<": "&lt;", ">": "&gt;", "&": "&amp;"}.get(ch, ch))
        i += 1

    return "".join(out)


def _wrap(s: str) -> str:
    """Parenthesise a fraction part when it is more than one atom."""
    plain = re.sub(r"<[^>]+>|&[a-zA-Z#0-9]+;", "x", s)
    return s if len(plain) <= 1 else f"({s})"


def inline_math(text: str) -> str:
    return re.sub(r"(?<!\\)\$([^$]+)\$", lambda m: math(m.group(1)), text)


# ---------------------------------------------------------------------------
# bibliography
# ---------------------------------------------------------------------------

def parse_bibliography(tex: str):
    """key -> (number, short author, year, rendered HTML reference).

    Entries are written as \bibitem[Author(Year)]{key} followed by \newblock
    fields: authors, title, venue, then this manuscript's own note saying what
    the paper takes from the work. The note is editorial rather than
    bibliographic, so it is dropped from the rendered reference.
    """
    block = tex.split(r"\begin{thebibliography}")[1].split(r"\end{thebibliography}")[0]
    out, order = {}, []
    for n, chunk in enumerate(re.split(r"\\bibitem", block)[1:], 1):
        m = re.match(r"\s*\[([^\]]*)\]\s*\{([^}]+)\}", chunk)
        if not m:
            continue
        label, key = m.group(1), m.group(2)
        am = re.match(r"(.*?)\((\d{4}[a-z]?)\)", label)
        author, year = (am.group(1).strip(), am.group(2)) if am else (label, "")
        # The label carries LaTeX accents and ties, and a textual citation
        # prints this name straight into the prose, so it is decoded here.
        # A BibTeX label also repeats the full author list after the year,
        # as in "Simon et al.(2017)Simon, Joo, ...", which is not wanted.
        author = accents(author).replace("~", " ").strip()
        parts = [p.strip() for p in chunk[m.end():].split(r"\newblock") if p.strip()]
        out[key] = {"n": n, "author": author, "year": year,
                    "fields": parts}
        order.append(key)
    return out, order


def render_reference(entry, accessed: str) -> str:
    """One reference in the site's format: bold authors, italic venue, link."""
    f = [clean_text(x) for x in entry["fields"]]
    authors = f[0].rstrip(".") if f else entry["author"]
    title = f[1].rstrip(".") if len(f) > 1 else ""
    rest = f[2:-1] if len(f) > 3 else f[2:]      # drop the editorial note
    venue = " ".join(x for x in rest if x).strip()

    url = ""
    for piece in entry["fields"]:
        u = re.search(r"\\url\{([^}]+)\}|\\href\{([^}]+)\}", piece)
        if u:
            url = u.group(1) or u.group(2)
            break
    if not url:
        a = re.search(r"arXiv:(\d{4}\.\d{4,5})", venue)
        if a:
            url = f"https://arxiv.org/abs/{a.group(1)}"

    # the link is rendered separately, so strip any copy of it from the venue
    venue = re.sub(r"<https?://[^>]*>", "", venue)
    venue = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", venue)
    # Markdown emphasis would show as asterisks once wrapped in <i>
    venue = re.sub(r"\*([^*]+)\*", r"\1", venue)
    # Removing the URL can leave ". ." behind, and rstrip(".,") stops at the
    # space between them. Strip trailing whitespace and punctuation together.
    venue = re.sub(r"\s+", " ", venue)
    venue = re.sub(r"[\s.,]+$", "", venue).strip()

    year = entry["year"].rstrip("abc")
    bits = [f"<b>{authors}</b>,"]
    if title:
        bits.append(f'"{title},"')
    if venue:
        bits.append(f"<i>{venue}</i>,")
    # the venue usually ends in the year already; do not print it twice
    if year and year not in venue:
        bits.append(f"{year},")
    line = " ".join(bits).rstrip(",")
    if url:
        line += f', <a href="{url}">{url}</a>'
    return line + f" [Accessed: {accessed}]."


# ---------------------------------------------------------------------------
# numbering, so every \ref resolves to what the compiled paper shows
# ---------------------------------------------------------------------------

def collect_numbers(body: str, shared=None):
    """label -> the number LaTeX would print for it.

    `shared` maps a theorem environment to the one whose counter it continues,
    as declared by \\newtheorem{corollary}[proposition]{Corollary}. Papers
    differ on this, so it is read from the source rather than assumed.
    """
    shared = shared or {}
    nums, sec, sub = {}, 0, 0
    counters = {}
    fig = tab = eq = 0
    # labels attach to whatever most recently opened
    token = re.compile(
        r"\\section\{|\\subsection\{|\\begin\{figure\}|\\begin\{table\}|"
        r"\\begin\{equation\}|\\begin\{proposition\}|\\begin\{corollary\}|"
        r"\\begin\{(?:" + "|".join(THEOREMS) + r")\}|"
        r"\\label\{([^}]+)\}")
    current = None
    for m in token.finditer(body):
        text = m.group(0)
        if text.startswith(r"\label"):
            if current:
                nums[m.group(1)] = current
            continue
        if text.startswith(r"\section"):
            sec, sub = sec + 1, 0
            current = str(sec)
        elif text.startswith(r"\subsection"):
            sub += 1
            current = f"{sec}.{sub}"
        elif "figure" in text:
            fig += 1
            current = str(fig)
        elif "table" in text:
            tab += 1
            current = str(tab)
        elif "equation" in text:
            eq += 1
            current = str(eq)
        else:
            for name in THEOREMS:
                if name in text:
                    key = shared.get(name, name)
                    counters[key] = counters.get(key, 0) + 1
                    current = str(counters[key])
                    break
    return nums


# ---------------------------------------------------------------------------
# text
# ---------------------------------------------------------------------------

NUMS = {}          # label -> printed number, filled by main()
EQN = [0]          # the running equation number, shared by both passes
BIB = {}           # key -> entry, filled by main()


ACCENTS = {
    '\\"a': "&auml;", '\\"o': "&ouml;", '\\"u': "&uuml;", '\\"A': "&Auml;",
    '\\"O': "&Ouml;", '\\"U': "&Uuml;", "\\'a": "&aacute;", "\\'e": "&eacute;",
    "\\'i": "&iacute;", "\\'o": "&oacute;", "\\'u": "&uacute;",
    "\\'E": "&Eacute;", "\\`a": "&agrave;", "\\`e": "&egrave;",
    "\\^a": "&acirc;", "\\^e": "&ecirc;", "\\^o": "&ocirc;",
    "\\~n": "&ntilde;", "\\~a": "&atilde;", "\\ss": "&szlig;",
}


def accents(t: str) -> str:
    """LaTeX accent escapes as HTML entities, with and without braces."""
    for tex, html in ACCENTS.items():
        t = t.replace(tex, html)
        # the braced spelling, \"{u}
        t = t.replace(tex[:2] + "{" + tex[2:] + "}", html)
    t = re.sub(r"\\c\{c\}", "&ccedil;", t)
    return t


def clean_text(t: str) -> str:
    """Prose LaTeX as HTML, leaving math to math()."""
    t = accents(t)
    t = inline_math(t)
    t = re.sub(r"\\textbf\{([^{}]*)\}", r"**\1**", t)
    t = re.sub(r"\\emph\{([^{}]*)\}", r"*\1*", t)
    t = re.sub(r"\\textit\{([^{}]*)\}", r"*\1*", t)
    t = re.sub(r"\\texttt\{([^{}]*)\}", r"`\1`", t)
    t = re.sub(r"\\href\{([^}]+)\}\{([^{}]*)\}", r"[\2](\1)", t)
    t = re.sub(r"\\url\{([^}]+)\}", r"<\1>", t)

    def ref(m):
        return NUMS.get(m.group(1), "?")
    t = re.sub(r"\\ref\{([^}]+)\}", ref, t)
    t = re.sub(r"\\eqref\{([^}]+)\}", lambda m: f"({ref(m)})", t)

    def citep(m):
        keys = [k.strip() for k in m.group(1).split(",")]
        return "".join(f"[[{BIB[k]['n']}]](#ref-{BIB[k]['n']})"
                       for k in keys if k in BIB)
    t = re.sub(r"\\citep\{([^}]+)\}", citep, t)

    def citet(m):
        k = m.group(1).split(",")[0].strip()
        e = BIB.get(k)
        if not e:
            return m.group(0)
        return f"{e['author']} [[{e['n']}]](#ref-{e['n']})"
    t = re.sub(r"\\citet\{([^}]+)\}", citet, t)

    t = t.replace(r"\%", "%").replace(r"\&", "&").replace(r"\$", "$")
    t = t.replace(r"\_", "_").replace(r"\#", "#")

    # A few spacing and symbol commands are used in prose rather than in maths,
    # notably to indent a table cell, so they never reach math(). Longest first,
    # or \qquad is eaten as \quad followed by a stray "quad".
    for cmd, html in ((r"\qquad", "&nbsp;&nbsp;&nbsp;&nbsp;"),
                      (r"\quad", "&nbsp;&nbsp;"),
                      (r"\ldots", "&hellip;"),
                      (r"\dots", "&hellip;"),
                      ("\\ ", " ")):
        t = t.replace(cmd, html)
    t = t.replace("{,}", ",").replace("~", " ")
    # the keywords line is content, not plumbing
    t = re.sub(r"\\keywords\{([^}]*)\}",
               lambda m: "**Keywords.** " + m.group(1).replace(r"\and", "&middot;"),
               t)
    t = re.sub(r"\\newblock\s*", "", t)
    # BibTeX line-breaking hints, which are not content
    t = re.sub(r"\\penalty\s*-?\d*", "", t)
    t = re.sub(r"\\natexlab\{[^}]*\}", "", t)
    t = re.sub(r"\\(providecommand|expandafter|csname|endcsname|urlstyle|begingroup|endgroup|relax|else|fi|Url|doi)\b", "", t)
    t = re.sub(r"---", "&mdash;", t)
    t = re.sub(r"(?<=\d)--(?=\d)", "&ndash;", t)
    # LaTeX spacing escapes that survive into prose, such as the thin space in
    # "53\,ms". The class must be escaped as \\ or the pattern matches a
    # literal bracket instead and leaves them all behind.
    t = re.sub(r"\\[,;:!]", " ", t)
    t = re.sub(r"[ \t]+", " ", t)
    return t.strip()


def convert_table(block: str, number: str, figdir: dict) -> str:
    """A booktabs tabular as a Markdown table, with the caption beneath it."""
    cap = re.search(r"\\caption\{(.*?)\}\s*\n?\\label", block, re.S)
    caption = clean_text(re.sub(r"\s+", " ", cap.group(1))) if cap else ""

    rows_md = []
    for tab in re.finditer(r"\\begin\{tabular\}\{([^}]*)\}(.*?)\\end\{tabular\}",
                           block, re.S):
        spec, guts = tab.group(1), tab.group(2)
        ncol = len(re.findall(r"[lcr]", spec))
        align = ["---:" if c == "r" else (":---:" if c == "c" else "---")
                 for c in re.findall(r"[lcr]", spec)]
        lines = []
        for raw in guts.split(r"\\"):
            raw = re.sub(r"\\(top|mid|bottom)rule"
                         r"|\\cmidrule(\([^)]*\))?(\{[^}]*\})?",
                         "", raw).strip()
            if not raw:
                continue
            cells = [clean_text(c.strip()) for c in raw.split("&")]
            cells = [re.sub(r"\\multicolumn\{\d+\}\{[^}]*\}\{(.*)\}", r"\1", c)
                     for c in cells]
            while len(cells) < ncol:
                cells.append("")
            lines.append("| " + " | ".join(cells[:ncol]) + " |")
        if not lines:
            continue
        head, body = lines[0], lines[1:]
        rows_md.append("\n".join([head, "|" + "|".join(align) + "|"] + body))

    out = "\n\n".join(rows_md)
    if caption:
        out += f"\n\n<p class=\"equation-note\"><b>Table {number}.</b> {caption}</p>"
    return out


def convert_figure(block: str, number: str, figdir: dict) -> str:
    """A figure as the site's Academic_Figure shortcode plus its caption."""
    cap = re.search(r"\\caption\{(.*?)\}\s*\n?\\label", block, re.S)
    caption = clean_text(re.sub(r"\s+", " ", cap.group(1))) if cap else ""
    lab = re.search(r"\\label\{([^}]+)\}", block)
    src = figdir.get(lab.group(1) if lab else "", "")
    alt = re.sub(r"<[^>]+>|\*\*|\*", "", caption)[:120].replace('"', "'")
    piece = f'{{{{< Academic_Figure src="{src}" alt="{alt}" align="center" >}}}}'
    if caption:
        piece += f"\n\n<p class=\"equation-note\"><b>Figure {number}.</b> {caption}</p>"
    return piece


# ---------------------------------------------------------------------------
# body
# ---------------------------------------------------------------------------

THEOREMS = ("proposition", "corollary", "definition", "theorem", "lemma",
            "remark")

ENVS = ("figure", "table", "equation", "proof", "enumerate", "description",
        "abstract", "tikzpicture", "tabular", "minipage", "itemize") + THEOREMS


def convert_body(body: str, figdir: dict) -> str:
    """The manuscript body as Markdown, in document order."""
    out, i = [], 0
    fig = tab = eq = prop = defn = 0

    pattern = re.compile(
        r"(?P<disp>\\\[)|"
        r"\\section\*?\{(?P<sec>[^}]*)\}|"
        r"\\subsection\*?\{(?P<sub>[^}]*)\}|"
        r"\\paragraph\{(?P<par>[^}]*)\}|"
        r"\\begin\{(?P<env>" + "|".join(ENVS) + r")\}")

    while i < len(body):
        m = pattern.search(body, i)
        if not m:
            out.append(clean_text_block(body[i:]))
            break
        out.append(clean_text_block(body[i:m.start()]))

        if m.group("disp") is not None:
            close = body.index("\\]", m.end())
            inner = body[m.end():close]
            out.append(f'\n<p class="equation">{math(inner)}</p>\n')
            i = close + 2
        elif m.group("sec") is not None:
            out.append(f"\n## {clean_text(m.group('sec'))}\n")
            i = m.end()
        elif m.group("sub") is not None:
            out.append(f"\n### {clean_text(m.group('sub'))}\n")
            i = m.end()
        elif m.group("par") is not None:
            out.append(f"\n**{clean_text(m.group('par'))}**")
            i = m.end()
        else:
            env = m.group("env")
            block, i = take_env(body, m.start(), env)
            if env == "figure":
                fig += 1
                out.append("\n" + convert_figure(block, str(fig), figdir) + "\n")
            elif env == "table":
                tab += 1
                out.append("\n" + convert_table(block, str(tab), figdir) + "\n")
            elif env == "equation":
                out.append(equation_html(strip_env(block, env)))
            elif env in THEOREMS:
                inner = strip_env(block, env)
                name = env.capitalize()
                if env == "definition":
                    defn += 1
                    num = defn
                else:
                    prop += 1
                    num = prop
                bracket = re.match(r"\s*\[([^\]]*)\]", inner)
                extra = ""
                if bracket:
                    extra = f" ({clean_text(bracket.group(1))})"
                    inner = inner[bracket.end():]
                inner = re.sub(r"\\label\{[^}]*\}", "", inner)
                out.append("\n" + blockquote(
                    f"**{name} {num}{extra}.** {convert_nested(inner).strip()}") + "\n")
            elif env == "proof":
                inner = strip_env(block, env)
                out.append(f"\n*Proof.* {convert_nested(inner).strip()} &#9633;\n")
            elif env == "enumerate":
                inner = strip_env(block, env)
                for n, item in enumerate(split_items(inner), 1):
                    out.append(f"\n{n}. {clean_text_block(item).strip()}")
                out.append("\n")
            elif env == "description":
                inner = strip_env(block, env)
                for item in split_items(inner):
                    lab = re.match(r"\s*\[(.*?)\]", item, re.S)
                    term = clean_text(lab.group(1)) if lab else ""
                    rest = item[lab.end():] if lab else item
                    out.append(f"\n- **{term}** {clean_text_block(rest).strip()}")
                out.append("\n")
            elif env == "abstract":
                inner = strip_env(block, env)
                out.append("\n## Abstract\n\n" + clean_text_block(inner).strip() + "\n")
            else:
                out.append("")          # tikz, tabular, minipage handled above
    return "".join(out)




def equation_html(inner: str) -> str:
    """A numbered equation, taking the next number in the shared sequence."""
    inner = re.sub(r"\\label\{[^}]*\}", "", inner)
    EQN[0] += 1
    return (f'\n<p class="equation">{math(inner)}</p>\n'
            f'<p class="equation-note">({EQN[0]})</p>\n')


def blockquote(text: str) -> str:
    """Quote every line, blank ones included.

    A blank line inside a blockquote ends it, so a theorem containing a list
    would spill its parts outside the quote unless each line is marked.
    """
    return "\n".join(f"> {ln}" if ln.strip() else ">"
                     for ln in text.split("\n"))


def convert_nested(inner: str) -> str:
    """Prose that may contain lists or display maths, as inside a theorem.

    Deliberately narrower than convert_body: it never meets a figure or a
    table, so it touches none of the counters those keep.
    """
    inner = re.sub(r"\\label\{[^}]*\}", "", inner)

    def disp(m):
        return f'\n\n<p class="equation">{math(m.group(1))}</p>\n\n'
    inner = re.sub(r"\\\[(.*?)\\\]", disp, inner, flags=re.S)

    # a numbered equation can sit inside a theorem, and must take its place in
    # the same sequence as the ones outside
    inner = re.sub(r"\\begin\{equation\}(.*?)\\end\{equation\}",
                   lambda m: "\n\n" + equation_html(m.group(1)) + "\n\n",
                   inner, flags=re.S)

    out, pos = [], 0
    for m in re.finditer(r"\\begin\{(enumerate|itemize)\}(.*?)\\end\{\1\}",
                         inner, re.S):
        out.append(clean_text_block(inner[pos:m.start()]))
        items = split_items(m.group(2))
        for n, item in enumerate(items, 1):
            bullet = f"{n}." if m.group(1) == "enumerate" else "-"
            out.append(f"\n{bullet} {clean_text_block(item).strip()}")
        out.append("\n")
        pos = m.end()
    out.append(clean_text_block(inner[pos:]))
    return "\n".join(p for p in out if p.strip())

def take_env(s: str, start: int, env: str):
    """The whole environment beginning at `start`, honouring nesting."""
    open_tag, close_tag = f"\\begin{{{env}}}", f"\\end{{{env}}}"
    depth, j = 0, start
    while j < len(s):
        if s.startswith(open_tag, j):
            depth += 1
            j += len(open_tag)
        elif s.startswith(close_tag, j):
            depth -= 1
            j += len(close_tag)
            if depth == 0:
                return s[start:j], j
        else:
            j += 1
    return s[start:], len(s)


def strip_env(block: str, env: str) -> str:
    return block[len(f"\\begin{{{env}}}"):-len(f"\\end{{{env}}}")]


def split_items(inner: str):
    parts = re.split(r"\\item", inner)
    return [p for p in parts[1:] if p.strip()]


def clean_text_block(t: str) -> str:
    """Prose that may span several paragraphs, with blank lines preserved."""
    t = re.sub(r"(?m)^\s*%.*$", "", t)
    t = re.sub(r"\\label\{[^}]*\}", "", t)
    paras = [clean_text(p) for p in re.split(r"\n\s*\n", t)]
    return "\n\n".join(p for p in paras if p)


# ---------------------------------------------------------------------------
# the post
# ---------------------------------------------------------------------------

STYLE = """<style>
/* Make images transparent on light backgrounds */
.post-content img {
    mix-blend-mode: multiply;
}

/* Dark mode: show original images with transparent backgrounds */
[data-theme="dark"] .post-content img {
    filter: none;
    mix-blend-mode: normal;
    border-radius: 8px;
    opacity: 0.95;
}

.equation {
    text-align: center;
    margin: 1.4rem 0;
    font-size: 1.05rem;
}

.equation-note {
    text-align: center;
    font-size: 0.85rem;
    color: #6c6c6c;
    margin-top: -0.9rem;
    margin-bottom: 1.4rem;
}

[data-theme="dark"] .equation-note {
    color: #9b9c9d;
}

/* General hover effect for all links in post content */
.post-content a {
    transition: all 0.3s ease;
}
.post-content a:hover {
    color: #767676;
    text-shadow: 0px 0px 0.5px #767676;
}

/* Dark mode hover effect (same colour) */
[data-theme="dark"] .post-content a:hover {
    color: #767676;
    text-shadow: 0px 0px 0.5px #767676;
}

/* Reference list */
.reference-container {
    margin-top: 1rem;
}
.reference-item {
    display: flex;
    gap: 0.6rem;
    margin-bottom: 0.7rem;
    line-height: 1.55;
}
.reference-num {
    flex-shrink: 0;
    color: inherit;
}
.reference-text {
    flex: 1;
}
</style>"""


def build(tex_path, out_path, title, date, summary, tags, card, links,
          figdir, accessed, citation_text, bibtex, bbl_path=None,
          header_note=""):
    global NUMS, BIB
    tex = pathlib.Path(tex_path).read_text(encoding="utf-8")
    body = tex.split("\\begin{document}")[1]
    # a BibTeX paper ends the body at \\bibliography{...}; one with an
    # embedded list ends it at \\begin{thebibliography}
    for marker in ("\\begin{thebibliography}", "\\bibliographystyle{",
                   "\\bibliography{",
                   "\\end{document}"):
        body = body.split(marker)[0]
    body = body.replace("\\maketitle", "")

    # A paper that uses BibTeX keeps its rendered bibliography in a .bbl rather
    # than inside the manuscript, so the entries are read from there instead.
    EQN[0] = 0
    BIB, order = parse_bibliography(
        pathlib.Path(bbl_path).read_text(encoding="utf-8") if bbl_path else tex)
    shared = dict(re.findall(r"\\newtheorem\{([^}]+)\}\[([^\]]+)\]", tex))
    NUMS = collect_numbers(body, shared)

    md = [
        "---",
        f'title: "{title}"',
        f"date: {date}",
        "draft: false",
        'author: "Amey Thakur"',
        f'summary: "{summary}"',
        "tags: [" + ", ".join(f'"{t}"' for t in tags) + "]",
        "ShowToc: true",
        "TocOpen: false",
        "---",
        "",
        STYLE,
        "",
        f'{{{{< Academic_Figure src="{card}" alt="Title card: {title}, by Amey Thakur." align="center" >}}}}',
        "",
        '<div align="center">',
        "",
        links,
        "",
        "</div>",
        "",
        # a one-line note above the abstract, used to point at the announced
        # arXiv version and the repository when those exist
        *([header_note, ""] if header_note else []),
        convert_body(body, figdir).strip(),
        "",
        "---",
        "",
        "## Citation",
        "",
        "**Please cite this work as:**",
        "",
        f'<pre style="white-space: pre-wrap;"><code>{citation_text}</code></pre>',
        "",
        "**Or use the BibTex citation:**",
        "",
        "```",
        bibtex.strip(),
        "```",
        "",
        "---",
        "",
        "## References",
        "",
        '<div class="reference-container">',
        "",
    ]

    for key in order:
        e = BIB[key]
        md.append('<div class="reference-item">')
        md.append(f'    <span class="reference-num">[{e["n"]}]</span>')
        md.append(f'    <span class="reference-text"><a id="ref-{e["n"]}"></a>'
                  f'{render_reference(e, accessed)}</span>')
        md.append("</div>")
        md.append("")

    md.append("</div>")

    text = "\n".join(md)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    pathlib.Path(out_path).write_text(text, encoding="utf-8")
    return text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tex", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    print("This module is driven by a per-paper build script; see build_galois_post.py")


if __name__ == "__main__":
    main()
