import socket

def echo_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        message = "Hello, Echo Server!"
        client_socket.sendall(message.encode('utf-8'))
        response = client_socket.recv(1024)
        print(f"Server responded: {response.decode('utf-8')}")

if __name__ == "__main__":
    echo_client()

