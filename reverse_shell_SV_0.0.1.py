import socket
buffer_size = 10240

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    server_socket.bind(('IP', 23232))
    server_socket.listen(5)

    while True:
        client_socket, addr = server_socket.accept()
        # while True:
        data=client_socket.recv(buffer_size).decode()

        data = my_input(f"[{addr[0]}] - {data}> ")
        
        client_socket.send(data.encode())

        data=client_socket.recv(buffer_size)
        if not data or data.decode('utf-8') == 'END':
            # print("END")
            break
        print(data.decode('utf-8'))
        break
    client_socket.close()

def my_input(string):
    while True:
        data = str(input(string))
        if data != "":
            return data
        
if __name__ == "__main__":
    while True:
        try:
            server()
        except ConnectionResetError:
            print("connection error")
            pass

