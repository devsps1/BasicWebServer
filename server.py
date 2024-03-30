import socket
import re
import threading
import time

pattern = r"GET\s+([^?\s]+)"
HOST = '127.0.0.1'                
PORT = 80              

def handleConnection(c, addr):
    with c:
        print(f'Connected by {addr}. {threading.current_thread().name}')
        rqst = c.recv(1024).decode()
        match = re.search(pattern, rqst)
        path = match.group(1)
        if(path == "/index.html" or path == "/"):
            # print("Path:", path)
            time.sleep(5)
            c.send(b'HTTP/1.1 200 OK\r\n\r\n')
            with open('www/index.html') as send_file:
                c.send(send_file.read().encode())
            c.send(b'\r\n')
        else:
            c.send(b'HTTP/1.1 404 Not Found\r\n\r\n')
        

if __name__ == "__main__":
    count = 1
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(20)
        while True:
            c, addr = s.accept()
            thread = threading.Thread(target=handleConnection, args=(c, addr), name=count)
            count = count + 1
            thread.start()
