#!/usr/bin/env python3
"""Fast structural checks for the generated Anderson Technologies site."""

from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
PAGES = [
    "index.html", "business.html", "support.html", "ai.html", "faq.html",
    "careers.html", "contact.html", "reviews.html", "thanks.html", "404.html",
]


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.missing_alt = []

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if "id" in data:
            self.ids.append(data["id"])
        if tag == "a" and "href" in data:
            self.links.append(data["href"])
        if tag == "img" and "alt" not in data:
            self.missing_alt.append(data.get("src", "(unknown image)"))


def main():
    errors = []
    parsed = {}

    for name in PAGES:
        path = ROOT / name
        if not path.exists():
            errors.append(f"missing page: {name}")
            continue
        text = path.read_text(encoding="utf-8")
        if "—" in text or "–" in text:
            errors.append(f"dash character found: {name}")
        if "fonts.googleapis.com" in text or "fonts.gstatic.com" in text:
            errors.append(f"external font request found: {name}")
        if "styles.css?v=38" not in text:
            errors.append(f"wrong CSS version: {name}")
        if name not in {"404.html", "thanks.html"} and '<link rel="canonical"' not in text:
            errors.append(f"missing canonical: {name}")
        if name not in {"about.html"} and '<meta name="viewport"' not in text:
            errors.append(f"missing viewport meta: {name}")
        if "<h5" in text:
            errors.append(f"heading-level skip found: {name}")

        parser = PageParser()
        parser.feed(text)
        parsed[name] = parser
        duplicates = [value for value, count in Counter(parser.ids).items() if count > 1]
        if duplicates:
            errors.append(f"duplicate IDs in {name}: {', '.join(duplicates)}")
        if parser.missing_alt:
            errors.append(f"images missing alt in {name}: {', '.join(parser.missing_alt)}")

    for source, parser in parsed.items():
        for href in parser.links:
            split = urlsplit(href)
            if split.scheme or href.startswith(("mailto:", "tel:", "sms:")):
                continue
            target_name = unquote(split.path) or source
            if target_name.startswith("/"):
                continue
            target = ROOT / target_name
            if not target.exists():
                errors.append(f"broken link in {source}: {href}")
                continue
            if split.fragment and target_name.endswith(".html") and target_name in parsed:
                if unquote(split.fragment) not in parsed[target_name].ids:
                    errors.append(f"missing anchor in {source}: {href}")

    if '<link rel="canonical" href="https://andersontechsupport.com/">' not in (ROOT / "index.html").read_text(encoding="utf-8"):
        errors.append("home canonical is not the root URL")
    for name in ("thanks.html", "404.html"):
        if 'content="noindex,follow"' not in (ROOT / name).read_text(encoding="utf-8"):
            errors.append(f"missing noindex: {name}")
    if 'id="privacy"' not in (ROOT / "faq.html").read_text(encoding="utf-8"):
        errors.append("FAQ privacy section is missing")
    for font in ("plus-jakarta-sans.woff2", "space-grotesk.woff2"):
        if not (ROOT / "assets" / "fonts" / font).exists():
            errors.append(f"missing self-hosted font: {font}")

    if errors:
        print("SITE CHECK FAILED")
        for error in sorted(set(errors)):
            print(f"- {error}")
        raise SystemExit(1)
    print(f"SITE CHECK PASSED: {len(PAGES)} pages, internal links, IDs, images, versions, and font policy")


if __name__ == "__main__":
    main()
