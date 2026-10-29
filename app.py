from http.server import HTTPServer, BaseHTTPRequestHandler

 

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)

        self.send_header('Content-type', 'text/plain')

        self.end_headers()

        self.wfile.write(b"Hello from POC Kubernetes Cluster!\n")

 

HTTPServer(('0.0.0.0', 5000), Handler).serve_forever()