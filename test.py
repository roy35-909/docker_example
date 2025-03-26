from http.server import SimpleHTTPRequestHandler, HTTPServer

class HelloWorldHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, World!")

if __name__ == "__main__":
    server_address = ("", 8080)  # Serve on all available interfaces at port 8080
    httpd = HTTPServer(server_address, HelloWorldHandler)
    print("Serving on port 8080...")
    httpd.serve_forever()