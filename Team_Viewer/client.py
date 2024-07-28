import socket

HOST, PORT = '127.0.0.1', 4455
addr = (HOST, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(addr)




if __name__ == "__main__":
    main()