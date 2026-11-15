"""Authenticated container ingress around the unchanged loopback-only backend."""
import hmac
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import sys
import tempfile
import threading
from urllib.error import HTTPError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from run import configure_ai, load_workspace, resolved_config, verify_files


def ingress_handler(inner_port, token):
    class Proxy(BaseHTTPRequestHandler):
        def log_message(self, *args): pass

        def respond(self, status, body):
            self.send_response(status)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            if self.command != 'HEAD': self.wfile.write(body)

        def handle_request(self):
            if self.path == '/health' and self.command in {'GET', 'HEAD'}:
                return self.respond(200, b'{"ready":true}')
            if not hmac.compare_digest(self.headers.get('X-Flame-Proxy-Token', ''), token):
                return self.respond(403, b'{"error":"Trusted Worker required"}')
            if self.command not in {'GET', 'HEAD', 'POST'} or not self.path.startswith('/') or self.path.startswith('//'):
                return self.respond(400, b'{"error":"Invalid request"}')
            if self.headers.get('Transfer-Encoding'):
                return self.respond(400, b'{"error":"Chunked input unsupported"}')
            try:
                size = int(self.headers.get('Content-Length', '0'))
                if size < 0 or size > 32768: raise ValueError()
            except ValueError:
                return self.respond(400, b'{"error":"Invalid body size"}')
            body = self.rfile.read(size) if self.command == 'POST' else None
            request = Request('http://127.0.0.1:' + str(inner_port) + self.path, data=body,
                headers={'Content-Type': self.headers.get('Content-Type', 'application/json')}, method=self.command)
            try:
                response = urlopen(request, timeout=240)
            except HTTPError as error:
                response = error
            except OSError:
                return self.respond(503, b'{"error":"Backend unavailable"}')
            with response:
                data = response.read()
                self.send_response(response.status)
                for key in ['Content-Type', 'Cache-Control', 'X-Content-Type-Options', 'Referrer-Policy']:
                    if response.headers.get(key): self.send_header(key, response.headers[key])
                self.send_header('Content-Length', str(len(data)))
                self.end_headers()
                if self.command != 'HEAD': self.wfile.write(data)

        do_GET = do_HEAD = do_POST = handle_request
    return Proxy


def main():
    token = os.environ.get('FLAME_PROXY_TOKEN', '')
    if len(token) < 32: raise ValueError('Set a FLAME_PROXY_TOKEN secret of at least 32 characters')
    mode = 'off' if os.environ.get('FLAME_OFFLINE_CHECK') == '1' else 'openai'
    verify_files(ROOT)
    configure_ai(mode)
    config = resolved_config(ROOT)
    workspace = load_workspace(ROOT)
    with tempfile.TemporaryDirectory(prefix='flame-container-') as temp:
        config_path = Path(temp) / 'config.json'
        config_path.write_text(json.dumps(config), encoding='utf-8')
        with workspace.make_integrated_server(config_path, 0) as inner:
            if mode == 'off': inner.workspace_ai = None
            threading.Thread(target=inner.serve_forever, daemon=True).start()
            with ThreadingHTTPServer(('0.0.0.0', int(os.environ.get('PORT', '8080'))),
                                     ingress_handler(inner.server_port, token)) as proxy:
                print('Flame Atlas container ready on port ' + str(proxy.server_port), flush=True)
                try: proxy.serve_forever()
                finally: inner.shutdown()


if __name__ == '__main__': main()
