#!/usr/bin/env python3
import http.server
import os
import socketserver
from pathlib import Path


ROOT = Path(__file__).resolve().parent
ENV_PATH = ROOT / ".env"
PORT = 8001


def load_env(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
      return values
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


ENV = load_env(ENV_PATH)


class GlobeHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        if self.path.split("?", 1)[0] in {"/config.js", "/api/config", "/api/config.js"}:
            api_key = ENV.get("GEOAPIFY_API_KEY", "")
            payload = f'window.__APP_CONFIG__ = {{ GEOAPIFY_API_KEY: "{api_key}" }};\n'
            encoded = payload.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/javascript; charset=utf-8")
            self.send_header("Content-Length", str(len(encoded)))
            self.end_headers()
            self.wfile.write(encoded)
            return
        return super().do_GET()


if __name__ == "__main__":
    with socketserver.TCPServer(("127.0.0.1", PORT), GlobeHandler) as server:
        print(f"Serving globe at http://127.0.0.1:{PORT}/globe.html")
        server.serve_forever()
