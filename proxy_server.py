import sys,socket
import time

HOST = "127.0.0.1"
PORT = 8001
BUFFER_SIZE = 4096

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
                #google_conn,google_addr = end.accept()
                message = conn.recv(BUFFER_SIZE)
                #send message given from localhost connection
                end.sendall(message)
                #print("message : ",message)
                #recieve data, wait a bit, then send it back
                #request_data = conn.recv(BUFFER_SIZE)
                # full_data = b""
                # while True:
                #     data = end.recv(BUFFER_SIZE)
                #     if not data:
                #         break
                #     full_data += data
                full_data = end.recv(BUFFER_SIZE)
                time.sleep(0.5)
                #send message back to 
                conn.sendall(full_data)
                conn.close()


if __name__ == "__main__":
    main()


