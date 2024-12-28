# py-vpn
Simple vpn simulation with python and docker
- [Introduction](#introduction)
- [KeyComponents](#key-components)
- [Features](#features)
- [Installation](#installation)
- [License](#license)

## Introduction
### Secure VPN System with Dockerized Microservices
- This project demonstrates a secure VPN communication system implemented using Dockerized microservices.
- It consists of three primary services—VPN Server, VPN Tunnel, and VPN Client—orchestrated with docker-compose to ensure seamless interaction within an isolated network.
- The system is designed for secure data transmission between a client and a server through an intermediary tunnel. Each component has a specific role, and all communications are secured using SSL certificates.

## Key Components
### VPN Server (`vpn_server`):
- Acts as the endpoint for secure communication.
- Accepts only connections forwarded from the vpn_tunnel service.
- Validates connections and handles client messages using SSL.

### VPN Tunnel  (`vpn_tunnel`):
- Acts as a proxy between the client and the server.
- Establishes an SSL-secured connection with the `vpn_server`.
- Relays messages bi-directionally between the `vpn_client` and the `vpn_server`.

### VPN Client (`vpn_client`):
- Initiates the communication by connecting to the `vpn_tunnel`.
- Sends and receives messages through the tunnel.

## Features

### Secure Communication:
- All messages between the client, tunnel, and server are encrypted using SSL.
- Uses a certificate (`server.crt`) and private key (`server.key`) for authentication and encryption.

### Dockerized Architecture:
- Each service is containerized for portability and scalability.
- Services communicate via an isolated Docker network.

### Role-based Access Control:
- The `vpn_server` only accepts connections from the `vpn_tunnel` service for enhanced security.

### Bi-directional Message Forwarding:
- The `vpn_tunnel` forwards client requests to the server and relays server responses back to the client.

## Installation

- Generate SSL Certificates (if you haven't already):

```openssl genpkey -algorithm RSA -out server.key```
```openssl req -new -key server.key -out server.csr```
```openssl x509 -req -in server.csr -signkey server.key -out server.crt```

- Build and Start Docker Containers:
```docker-compose build ```
```docker-compose up```

## License

This project is licensed under the [MIT License](LICENSE).

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
