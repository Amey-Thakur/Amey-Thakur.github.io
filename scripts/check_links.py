#!/usr/bin/env python3
"""Check every link in the site's content.

Two kinds of failure matter here and they are checked separately:

  relative  A link to a file inside the post's own bundle. If the file is not
            there the reader gets a 404 on the site itself. Always checked,
            needs no network, and is what the deploy gate runs.

  external  A link off the site. Checked only with --external, because a
            remote host being slow or rate-limiting is not a reason to fail a
            deploy. Run it by hand when auditing.

    python scripts/check_links.py                    # relative links only
    python scripts/check_links.py --external         # also check the network
    python scripts/check_links.py --external --json  # machine-readable report

Standard library only.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"

# Markdown links and images, plus raw HTML src/href.
LINK = re.compile(
    r'!?\[[^\]]*\]\(\s*<?([^)\s>]+)>?[^)]*\)'
    r'|<img[^>]+src="([^"]+)"'
    r'|href="([^"]+)"'
)

SKIP_PREFIX = ("#", "mailto:", "data:", "tel:", "javascript:")

UA = {"User-Agent": "Mozilla/5.0 (compatible; ameyarc-link-check)"}


FENCE = re.compile(r"^\s*(```|~~~)", re.M)


def strip_code(text: str) -> str:
    """Blank out fenced and inline code before looking for links.

    A post that shows HTML source contains things that look exactly like
    links and are not. Leaving them in made the checker report five broken
    links in one article, every one of them a line of example markup.
    """
    out, fence = [], False
    for line in text.splitlines():
        if FENCE.match(line):
            fence = not fence
            out.append("")
            continue
        out.append("" if fence else line)
    joined = "\n".join(out)
    # Inline code spans can carry the same false positives.
    return re.sub(r"`[^`\n]*`", "", joined)


def is_rendered(md: Path) -> bool:
    """Is this markdown file actually published as a page?

    Inside a leaf bundle, the bundle's index.md is the page and every other
    markdown file is a page resource that Hugo never renders. Archived project
    reports sit in those bundles, and their internal references are not links
    the reader can ever follow, so gating a deploy on them would be noise.
    """
    if md.name in ("index.md", "_index.md"):
        return True
    for parent in md.parents:
        if parent == CONTENT:
            break
        if (parent / "index.md").exists():
            return False
    return True


def targets():
    """Yield (markdown file, raw link) for every rendered page in the content tree."""
    for md in sorted(CONTENT.rglob("*.md")):
        if not is_rendered(md):
            continue
        text = strip_code(md.read_text(encoding="utf-8", errors="ignore"))
        for m in LINK.finditer(text):
            raw = m.group(1) or m.group(2) or m.group(3)
            if raw and not raw.startswith(SKIP_PREFIX):
                yield md, raw.strip()


def check_relative(md: Path, raw: str):
    """Resolve a relative link against the post bundle it appears in."""
    path = urllib.parse.unquote(raw.split("#")[0].split("?")[0])
    if not path:
        return None
    # Site-absolute links are resolved by the engine, not the file system.
    if path.startswith("/"):
        return None
    resolved = (md.parent / path).resolve()
    return None if resolved.exists() else path


def check_url(url: str):
    """Return None when reachable, otherwise a short reason."""
    req = urllib.request.Request(url, headers=UA, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            return None if r.status < 400 else f"HTTP {r.status}"
    except urllib.error.HTTPError as e:
        # Several hosts refuse automated requests but serve humans fine.
        if e.code in (403, 405, 429):
            return None
        return f"HTTP {e.code}"
    except Exception as e:
        return type(e).__name__


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--external", action="store_true",
                    help="also check links that leave the site")
    ap.add_argument("--json", action="store_true", help="emit a JSON report")
    args = ap.parse_args()

    rel_bad, ext = [], {}
    seen_rel = 0
    for md, raw in targets():
        if raw.startswith("http"):
            ext.setdefault(raw, []).append(str(md.relative_to(ROOT)).replace("\\", "/"))
            continue
        seen_rel += 1
        missing = check_relative(md, raw)
        if missing:
            rel_bad.append({"file": str(md.relative_to(ROOT)).replace("\\", "/"),
                            "link": raw})

    ext_bad = []
    if args.external and ext:
        with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
            for url, reason in zip(ext, pool.map(check_url, ext)):
                if reason:
                    ext_bad.append({"url": url, "reason": reason, "in": ext[url]})

    if args.json:
        print(json.dumps({"relative_checked": seen_rel, "relative_broken": rel_bad,
                          "external_checked": len(ext) if args.external else 0,
                          "external_broken": ext_bad}, indent=2))
    else:
        print(f"relative links checked : {seen_rel}")
        print(f"relative links broken  : {len(rel_bad)}")
        for b in rel_bad:
            print(f"    {b['file']}\n      -> {b['link']}")
        if args.external:
            print(f"external links checked : {len(ext)}")
            print(f"external links broken  : {len(ext_bad)}")
            for b in sorted(ext_bad, key=lambda x: x["url"]):
                print(f"    {b['reason']:<12} {b['url']}")
                for f in b["in"][:3]:
                    print(f"                 in {f}")

    # Only relative links gate the build. A remote host having a bad day is
    # not a reason to refuse to publish.
    return 1 if rel_bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
