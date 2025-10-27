import socket

def start_udp_server():
    server_ip = '127.0.0.1'
    server_port = 2000
    buffer_size = 1024

    try:
        # Create UDP socket
        udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_server_socket.bind((server_ip, server_port))
        print(f"UDP server listening on {server_ip}:{server_port}")

        while True:
            # Receive data from client
            data, client_address = udp_server_socket.recvfrom(buffer_size)
            message = data.decode()
            print(f"Received '{message}' from {client_address}")

            # Send response back to client
            udp_server_socket.sendto(b"Got it!", client_address)

    except Exception as e:
        print(f"Server error: {e}")
    finally:
        udp_server_socket.close()
        print("UDP server socket closed.")

if __name__ == "__main__":
    start_udp_server()