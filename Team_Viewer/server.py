import socket
HOST, PORT = "127.0.0.1", 4455
ADDR = (HOST, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
    print("[STARTING] server is starting.")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    while True:
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")


if __name__ == "__main__":
    main()
