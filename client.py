import socket

def start_client():
    host = '127.0.0.1'  # server address
    port = 65432        # server port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            print(f"Connected to server at {host}:{port}")
            message = "Hello, Server!"
            s.sendall(message.encode())
            data = s.recv(1024)
            print(f"Received from server: {data.decode()}")
        except ConnectionRefusedError:
            print("Failed to connect: Server is not running.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    start_client()
