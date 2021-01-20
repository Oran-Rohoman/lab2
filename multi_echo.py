import sys,socket
import time
from multiprocessing import Process

HOST = "127.0.0.1"
PORT = 8001
BUFFER_SIZE = 4096

def handle_req(conn,addr):
    client_data = conn.recv(BUFFER_SIZE)
    conn.sendall(client_data)
    print(client_data)

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
            p = Process(target=handle_req, args=(conn, addr))
            p.daemon = True
            p.start()
            #send message back to 
            
            conn.close()


if __name__ == "__main__":
    main()


