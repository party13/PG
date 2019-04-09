import socket
import settings


def server_side():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', settings.PORT))

    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        print('connection from ', addr)

        while True:
            request = client_socket.recv(36)

            if not request:
                break
            else:
                response = 'received string with {} length'.format(len(request))
                print(response)
                client_socket.send(response)