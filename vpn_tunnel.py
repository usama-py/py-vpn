import socket
import ssl
import threading

# Configuration
LISTEN_HOST = '0.0.0.0'  # Listen on all available interfaces
LISTEN_PORT = 8080       # Port to listen for incoming connections
SERVER_HOST = 'host.docker.internal'  # VPN server host
SERVER_PORT = 8000           # VPN server port

# SSL context for securing the connection to the VPN server
def create_ssl_connection_to_server():
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_verify_locations(cafile="server.crt")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_connection = context.wrap_socket(client_socket, server_hostname=SERVER_HOST)
    ssl_connection.connect((SERVER_HOST, SERVER_PORT))

    return ssl_connection

def handle_client_connection(client_socket: socket):
    try:
        # Establish SSL connection to the VPN server
        print(f"Forwarding client connection to {SERVER_HOST}:{SERVER_PORT}")
        server_connection = create_ssl_connection_to_server()

        # Receive data from the client and forward it to the server
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            server_connection.sendall(data)

            # Receive response from the server and forward it back to the client
            server_response = server_connection.recv(1024)
            if server_response:
                client_socket.sendall(server_response)
            else:
                break
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close connections
        client_socket.close()
        server_connection.close()

def start_proxy_server():
    # Create a TCP/IP socket to listen for client connections
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((LISTEN_HOST, LISTEN_PORT))
    server_socket.listen(5)
    print(f"Listening for incoming connections on {LISTEN_HOST}:{LISTEN_PORT}")

    # Accept and handle incoming client connections in a new thread
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        client_thread = threading.Thread(target=handle_client_connection, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_proxy_server()
