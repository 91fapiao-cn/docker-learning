from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os


def get_port() -> int:
    return int(os.environ.get('PORT', '8000'))


def make_body(path: str) -> dict:
    port = get_port()
    if path == '/healthz':
        return {
            'ok': True,
            'status': 'healthy',
            'port': port,
            'path': path,
        }
    return {
        'ok': True,
        'message': 'hello from docker-learning',
        'port': port,
        'path': path,
    }


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = make_body(self.path)
        data = json.dumps(body).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, format, *args):
        return


def main() -> None:
    port = get_port()
    print(f'Starting server on 0.0.0.0:{port}', flush=True)
    HTTPServer(('0.0.0.0', port), Handler).serve_forever()


if __name__ == '__main__':
    main()
