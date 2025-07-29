# app/main.py
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from app.model_clip import generate_embedding
from io import BytesIO
from PIL import Image

class SimpleHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/embed":
            self.send_error(404, "Endpoint no encontrado")
            return

        content_length = int(self.headers['Content-Length'])
        file_data = self.rfile.read(content_length)

        # Guardar temporal
        os.makedirs("/tmp", exist_ok=True)
        temp_path = "/tmp/uploaded_image.jpg"
        with open(temp_path, "wb") as f:
            f.write(file_data)

        # Generar embedding
        embedding = generate_embedding(temp_path)

        # Responder
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"embedding": embedding}).encode())

def run(server_class=HTTPServer, handler_class=SimpleHandler, port=8002):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Servicio CNN corriendo en puerto {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
