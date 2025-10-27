import socket

def start_tcp_server():
    server_ip = '127.0.0.1'
    server_port = 13000
    buffer_size = 1024

    try:
        # Create TCP socket
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.bind((server_ip, server_port))
        tcp_server_socket.listen(1)
        print(f"TCP server listening on {server_ip}:{server_port}")

        conn, addr = tcp_server_socket.accept()
        print(f"Connection established with {addr}")

        data = conn.recv(buffer_size).decode()
        print(f"Received: {data}")

        if data.isdigit():
            result = "Even" if int(data) % 2 == 0 else "Odd"
        else:
            result = "Invalid input"

        conn.send(result.encode())
        conn.close()
        print("Connection closed.")

    except Exception as e:
        print(f"Server error: {e}")
    finally:
        tcp_server_socket.close()
        print("TCP server socket closed.")

if __name__ == "__main__":
    start_tcp_server()