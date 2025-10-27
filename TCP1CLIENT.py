import socket

def tcp_client():
    server_ip = '127.0.0.1'
    server_port = 13000
    buffer_size = 1024

    try:
        # Create TCP socket
        tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_client_socket.connect((server_ip, server_port))
        print(f"Connected to TCP server at {server_ip}:{server_port}")

        number = input("Enter a number: ")
        tcp_client_socket.send(number.encode())

        response = tcp_client_socket.recv(buffer_size)
        print("Server response:", response.decode())

    except Exception as e:
        print(f"Client error: {e}")
    finally:
        tcp_client_socket.close()
        print("TCP client socket closed.")

if __name__ == "__main__":
    tcp_client()