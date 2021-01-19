import socket
import sys

def get_remote_ip(host):
    print("getting IP for host")
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("host name could not be resolved")
        sys.exit()
    print("IP address of {host} us {remote_ip}")
    return remote_ip

def create_tcp_socket():
    print('Creating socket')
    try:
        s = socket.socket(socket.AF_INET, socker.SOCK_STREAM)
    except(socker.error, msg):
        print("failed")
        sys.exit()
    print("succ")
    return s

def send_data(serversocket, payload):
    print("sending payload")
    try: 
        serversocket.sendall(payload.encode())
    except socket.error:
        sys.exit()
    print("payload sent")


def main():
    
    try:
        host = "www.google.com"
        port = 80
        payload = f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'
        buffer_size = 4096
        s = create_tcp_socket()
        remote_ip = get_remote_ip(host)
        s.connect((remote_ip, port))
        send_data(s,payload)
        s.shutdown(socket.SHUT_WR)
        full_data = b""
        while True:
            data = s.recv(buffer_size)
            if not data:
                break
            full_data += data
            print(full_data)
        except Exception as e:
            print(e)
        finally:
            s.close()

if __name__ == "__main__":
    main()
