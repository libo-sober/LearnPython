import socketserver
import time

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        while True:
            try:
                content = conn.recv(1024).decode('utf-8')
                conn.send(content.upper().encode('utf-8'))
                time.sleep(0.5)
            except ConnectionResetError:
                break


server = socketserver.ThreadingTCPServer(('127.0.0.1', 9000), Myserver)
server.serve_forever()



