
import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

# Render ፖርት እንዲያገኝ የሚረዳ ቀላል ሰርቨር
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running!")

def run_dummy_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    server.serve_forever()

# ሰርቨሩን በ Background ማነሳት
threading.Thread(target=run_dummy_server, daemon=True).start()
