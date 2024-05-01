from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import time

# Define el puerto en el que escuchará el servidor
PORT = 8000

# Define el manejador de solicitudes HTTP
class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        # Lee los datos del archivo adjunto
        data = self.rfile.read(content_length)
        # Guarda el archivo en el servidor
        with open('payload.exe', 'wb') as file:
            file.write(data)
        print('===========Running scanning===========')
        time.sleep(2)
        os.system("python Extractor/PE_main.py {} > analysis.txt".format('payload.exe'))
        # Lee el contenido de analysis.txt
        with open('analysis.txt', 'r') as analysis_file:
            analysis_content = analysis_file.read()
        # Responde al cliente con el contenido de analysis.txt
        self.send_response(200)
        self.end_headers()
        self.wfile.write(analysis_content.encode('utf-8'))

# Crea una instancia del servidor HTTP
server = HTTPServer(('localhost', PORT), RequestHandler)


def start():
    # Inicia el servidor y manténlo en ejecución
    print(f'Servidor escuchando en el puerto {PORT}...')
    server.serve_forever()

if __name__ == '__main__':
    start()
