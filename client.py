import sys
import socket

def client_program():

    if len(sys.argv) != 2:
        print("Usage: python3 client.py <hostname>")
        sys.exit(1)


    host = sys.argv[1].strip()
    port = 5000 

    print("Connecting to server at:", host)

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input(" -> ")

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        print('Received from server: ' + data)

        message = input(" -> ")  

    client_socket.close() 

if __name__ == '__main__':
    client_program()

