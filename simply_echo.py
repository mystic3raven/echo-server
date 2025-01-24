import socket

def echo_server(host='127.0.0.1', port=65432):
    """A simple echo server that echoes back any received string."""
    try:
        # Create a TCP/IP socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the address and port
        server_socket.bind((host, port))
        print(f"Server started at {host}:{port}")

        # Listen for incoming connections
        server_socket.listen(1)
        print("Waiting for a connection...")

        while True:
            # Accept a new connection
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")

            with client_socket:
                while True:
                    # Receive data from the client
                    data = client_socket.recv(1024)
                    if not data:
                        # Break the loop if no data is received (client disconnected)
                        break

                    print(f"Received: {data.decode('utf-8')}")

                    # Echo the data back to the client
                    client_socket.sendall(data)
                    print(f"Echoed: {data.decode('utf-8')}")

    except KeyboardInterrupt:
        print("\nServer shutting down...")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    echo_server()

