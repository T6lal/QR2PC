import http.server
import webbrowser
import socketserver
import urllib.parse
import socket

PORT = 8787

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith("/open?url="):
            url = self.path[len("/open?url="):]
            # Decode URL
            url = urllib.parse.unquote(url)
            print(f"Opening URL: {url}")
            webbrowser.open(url)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'URL opened on PC')
        else:
            self.send_response(404)
            self.end_headers()
    
    def log_message(self, format, *args):
        # Disable default log messages
        return

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

ip = get_ip()
print(f"Server started on IP: {ip}, port: {PORT}")
print(f"Use this URL in your Shortcut: http://{ip}:{PORT}/open?url=")
print("Waiting for links from iPhone...")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()