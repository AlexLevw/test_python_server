from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "localhost"
PORT = 8080

class MainHTTP(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>My HTTP Sever</h1></body></html>", "utf-8"))


server = HTTPServer((HOST, PORT), MainHTTP)
server.serve_forever()
server.server_close()