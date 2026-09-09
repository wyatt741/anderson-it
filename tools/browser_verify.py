#!/usr/bin/env python3
"""Render and interaction checks for the generated site using local Chrome."""

import json
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
BASE = "http://127.0.0.1:8765"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PAGES = [
    "index.html", "business.html", "support.html", "ai.html", "faq.html",
    "careers.html", "contact.html", "reviews.html", "thanks.html", "404.html",
]
WIDTHS = [(1440, 1000), (430, 932), (320, 720)]


def main():
    failures = []
    report = []
    shot_dir = ROOT / "Backups" / "browser-check-2026-09-09"
    shot_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True, executable_path=CHROME)
        for width, height in WIDTHS:
            context = browser.new_context(
                viewport={"width": width, "height": height},
                reduced_motion="reduce",
                color_scheme="dark",
            )
            for name in PAGES:
                page = context.new_page()
                page_errors = []
                resource_errors = []
                page.on("pageerror", lambda error, bag=page_errors: bag.append(str(error)))
                page.on("response", lambda response, bag=resource_errors: bag.append(f"{response.status} {response.url}") if response.url.startswith(BASE) and response.status >= 400 else None)
                response = page.goto(f"{BASE}/{name}", wait_until="networkidle")
                if not response or not response.ok:
                    failures.append(f"{name} at {width}px returned {getattr(response, 'status', 'no response')}")
                    page.close()
                    continue

                metrics = page.evaluate(r"""() => {
                  const root = document.documentElement;
                  const body = document.body;
                  const vw = root.clientWidth;
                  const overflowers = [...document.querySelectorAll('body *')].filter(el => {
                    const style = getComputedStyle(el);
                    if (style.position === 'fixed' || style.position === 'absolute') return false;
                    const rect = el.getBoundingClientRect();
                    return rect.left < -1 || rect.right > vw + 1;
                  }).slice(0, 10).map(el => `${el.tagName.toLowerCase()}.${String(el.className || '').trim().replace(/\s+/g,'.')}`);
                  const smallTargets = [...document.querySelectorAll('a,button,input,select,textarea,summary')].filter(el => {
                    const rect = el.getBoundingClientRect();
                    const style = getComputedStyle(el);
                    return style.visibility !== 'hidden' && style.display !== 'none' && rect.width > 0 && rect.height > 0 && (rect.width < 24 || rect.height < 24);
                  }).slice(0, 10).map(el => `${el.tagName.toLowerCase()}.${String(el.className || '').trim().replace(/\s+/g,'.')}:${Math.round(el.getBoundingClientRect().width)}x${Math.round(el.getBoundingClientRect().height)}`);
                  return {
                    clientWidth: vw,
                    scrollWidth: Math.max(root.scrollWidth, body.scrollWidth),
                    overflowers,
                    smallTargets,
                    theme: root.getAttribute('data-theme'),
                  };
                }""")
                report.append({"page": name, "width": width, **metrics})
                if metrics["scrollWidth"] > metrics["clientWidth"]:
                    failures.append(f"horizontal overflow: {name} at {width}px ({metrics['scrollWidth']} > {metrics['clientWidth']}), {metrics['overflowers']}")
                if page_errors:
                    failures.append(f"script errors: {name} at {width}px: {page_errors}")
                if resource_errors:
                    failures.append(f"resource errors: {name} at {width}px: {resource_errors}")
                if metrics["theme"] != "dark":
                    failures.append(f"wrong default theme: {name} at {width}px")

                if (name, width) in {("index.html", 1440), ("index.html", 430), ("contact.html", 430), ("faq.html", 430), ("careers.html", 320)}:
                    page.screenshot(path=str(shot_dir / f"{Path(name).stem}-{width}.png"), full_page=True)
                page.close()

            context.close()

        context = browser.new_context(viewport={"width": 430, "height": 932}, reduced_motion="reduce")
        page = context.new_page()
        page.goto(f"{BASE}/index.html", wait_until="networkidle")
        page.click(".burger")
        menu_state = page.evaluate("""() => ({
          open: document.body.classList.contains('menu-open'),
          expanded: document.querySelector('.burger').getAttribute('aria-expanded'),
          activeInside: document.querySelector('#mobile-menu').contains(document.activeElement),
          mainInert: document.querySelector('main').inert,
        })""")
        if menu_state != {"open": True, "expanded": "true", "activeInside": True, "mainInert": True}:
            failures.append(f"mobile menu state failed: {menu_state}")
        page.keyboard.press("Escape")
        if page.evaluate("document.activeElement !== document.querySelector('.burger') || document.body.classList.contains('menu-open')"):
            failures.append("mobile menu did not close and return focus on Escape")

        before = page.get_attribute("html", "data-theme")
        page.click(".burger")
        page.click(".mobile-menu .theme-toggle")
        after = page.get_attribute("html", "data-theme")
        if before == after or after != "light":
            failures.append(f"theme toggle failed: {before} to {after}")
        context.close()

        context = browser.new_context(viewport={"width": 430, "height": 932}, reduced_motion="reduce")
        page = context.new_page()
        page.goto(f"{BASE}/contact.html?job=Systems%20Engineer", wait_until="networkidle")
        if "Systems Engineer" not in page.input_value("#message") or "Careers: Systems Engineer" != page.input_value("#service"):
            failures.append("career application prefill failed")
        accepts = page.get_attribute("#photos", "accept") or ""
        if ".pdf" not in accepts or ".docx" not in accepts:
            failures.append("resume attachment types are missing")
        context.close()

        context = browser.new_context(viewport={"width": 430, "height": 932}, reduced_motion="reduce")
        page = context.new_page()
        page.goto(f"{BASE}/contact.html", wait_until="networkidle")
        page.evaluate("document.querySelector('#contact-form').action = 'http://127.0.0.1:8766/submit'")
        page.fill("#name", "Browser Test")
        page.fill("#email", "browser-test@example.com")
        page.fill("#message", "Form confirmation test")
        page.click("#contact-form button[type=submit]")
        page.wait_for_timeout(300)
        if "Sending" not in page.text_content("#form-status"):
            failures.append("contact form reported success before the same-origin confirmation page")
        try:
            page.wait_for_function("document.querySelector('#form-status').textContent.includes('was sent')", timeout=5000)
        except Exception:
            failures.append("contact form did not confirm the same-origin success redirect")
        if page.input_value("#name"):
            failures.append("contact form did not reset after confirmed delivery")
        context.close()
        browser.close()

    (shot_dir / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    if failures:
        print("BROWSER CHECK FAILED")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)
    print(f"BROWSER CHECK PASSED: {len(report)} page and viewport combinations")
    print(f"Screenshots: {shot_dir}")


if __name__ == "__main__":
    main()
