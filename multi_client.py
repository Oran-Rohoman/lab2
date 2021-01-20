import socket, sys
from multiprocessing import Pool


def create_tcp_socket():
    print('Creating socket')
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except (socket.error, msg):
        print(f'Failed to create socket. Error code: {str(msg[0])} , Error message : {msg[1]}')
        sys.exit()
    print('Socket created successfully')
    return s

def send_data(serversocket, payload):
    print("Sending payload")    
    try:
        serversocket.sendall(payload.encode())
    except socket.error:
        print ('Send failed')
        sys.exit()
    print("Payload sent successfully")
def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    print (f'Ip address of {host} is {remote_ip}')
    return remote_ip

def connect(addr):
    host = '127.0.0.1'
    google = 'www.google.com'
    port = 8001
    payload = f'GET / HTTP/1.0\r\nHost: {google}\r\n\r\n'
    buffer_size = 4096
    s = create_tcp_socket()
    s.connect(addr) 
    send_data(s, payload)
    s.shutdown(socket.SHUT_WR)

    #continue accepting data until no more left
    full_data = b''
    while True:
        data = s.recv(buffer_size)
        if not data:
            break
        full_data += data
    print(full_data)


def main():
    address = [('127.0.0.1',8001)]
    with Pool() as p:
        p.map(connect,address *10)



if __name__ == "__main__":
    main()
