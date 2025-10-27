import socket

def udp_client():
    server_ip = '127.0.0.1'
    server_port = 2000
    buffer_size = 1024

    try:
        # Create UDP socket
        udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Send message to server
        message = input("Enter a message to send to the server: ")
        udp_client_socket.sendto(message.encode(), (server_ip, server_port))

        # Set timeout to avoid hanging
        udp_client_socket.settimeout(5)

        # Receive response from server
        response, _ = udp_client_socket.recvfrom(buffer_size)
        print("Server response:", response.decode())

    except socket.timeout:
        print("No response from server. Request timed out.")
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        udp_client_socket.close()
        print("UDP client socket closed.")

if __name__ == "__main__":
    udp_client()