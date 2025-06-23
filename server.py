import socket

def start_server():
    host = '127.0.0.1'  # localhost
    port = 65432        # non-privileged port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}...")

        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    print("Client disconnected.")
                    break
                print(f"Received from client: {data.decode()}")
                conn.sendall(b"Message received")

if __name__ == "__main__":
    start_server()

