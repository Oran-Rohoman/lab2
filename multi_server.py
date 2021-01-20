import sys,socket
import time
from multiprocessing import Process

HOST = "127.0.0.1"
PORT = 8001
BUFFER_SIZE = 4096

def handle_req(conn,addr,end):
    client_data = conn.recv(BUFFER_SIZE)
    end.sendall(client_data)
    end.shutdown(socket.SHUT_WR)
    google_response = end.recv(BUFFER_SIZE)
    conn.sendall(google_response)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as start:
        host = "www.google.com"
        port = 80
        #QUESTION 3
        start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        remote_ip = socket.gethostbyname( HOST )
        
        #bind socket to address
        start.bind((HOST, PORT))
        #set to listening mode
        start.listen(2)
        
        #continuously listen for connections
        while True:
            conn, addr = start.accept()
            print("Connected by", addr)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as end:
                remote_ip = socket.gethostbyname(host)
                # connect to google on port 80
                end.connect((remote_ip,port))
                p = Process(target=handle_req, args=(conn, addr, end))
                p.daemon = True
                p.start()
                #send message back to 
                
            conn.close()


if __name__ == "__main__":
    main()


