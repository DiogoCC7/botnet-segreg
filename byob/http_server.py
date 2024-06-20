import os
import json

from http.server import HTTPServer, BaseHTTPRequestHandler

# Create an Simple HTTP SERVER
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """
        Payload file path, this file is meant to be uploaded to the victim machine
        this will allow that the machine would be capable to manage multiple requests
        to an respective server.
    """
    
    payload_path = "payload.py"

    def json(self, body, status: int = 200):
        """
            Send json object with standards http headers
        """

        self.send_response(status)
        
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        self.wfile.write(json.dumps(body).encode())

    def do_GET(self):
        if not os.path.exists(self.payload_path):
            return self.json({
                "message": "file not found"
            })
        
        file_size = os.path.getsize(self.payload_path)
                
        self.send_response(200)
        self.send_header('Content-type', 'application/octet-stream')
        self.send_header('Content-Disposition', f'attachment; filename="{os.path.basename(self.payload_path)}"')
        self.send_header('Content-Length', str(file_size))
        self.end_headers()
        
        with open(self.payload_path, 'rb') as file:
            self.wfile.write(file.read())
            file.close()

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=3000):
    server_address = ('0.0.0.0', port)
    httpd = server_class(server_address, handler_class)
    
    print(f"Starting httpd server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    # Run the actual server
    run()
