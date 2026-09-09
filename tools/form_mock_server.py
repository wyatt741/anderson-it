#!/usr/bin/env python3
"""Cross-origin form target used only by browser_verify.py."""

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("content-length", 0))
        if length:
            self.rfile.read(length)
        body = b"""<!doctype html><meta charset=utf-8><title>Queued</title>
<script>setTimeout(function(){location.href='http://127.0.0.1:8765/thanks.html'},1000)</script>"""
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *_):
        pass


if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", 8766), Handler).serve_forever()
