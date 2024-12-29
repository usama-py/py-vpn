import socket
import ssl

# Configuration
HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 8000        # Port to listen on

def start_server():
    # Create a plain socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Server listening on {HOST}:{PORT}", flush=True)

    # Create SSL context
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")

    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        client_ip = client_address[0]
        print(f"Connection from {client_ip}", flush=True)

        # Wrap the socket with SSL for secure communication
        ssl_socket = context.wrap_socket(client_socket, server_side=True)

        try:
            data = ssl_socket.recv(1024)
            print(f"Received: {data.decode('utf-8')}", flush=True)
            # Send a response back
            ssl_socket.sendall(b"Hello from VPN Server!")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            ssl_socket.close()

if __name__ == "__main__":
    start_server()
