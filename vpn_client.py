import socket

# Configuration
PROXY_HOST = 'vpn_tunnel'  # The address of the proxy server (where the proxy listens)
PROXY_PORT = 8080          # The port the proxy listens on (as set in the proxy server)

def start_client():
    # Create a plain socket to connect to the proxy
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the proxy server (no SSL needed here)
    print(PROXY_HOST, PROXY_PORT)
    client_socket.connect((PROXY_HOST, PROXY_PORT))
    print(f"Connected to proxy at {PROXY_HOST}:{PROXY_PORT}")

    # Send a message to the proxy (which will forward it to the VPN server)
    message = "Hello from Client, via Proxy!"
    client_socket.sendall(message.encode('utf-8'))

    # Receive the response from the proxy (which will forward it back from the VPN server)
    response = client_socket.recv(1024)
    print(f"Received from server through proxy: {response.decode('utf-8')}")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client()
