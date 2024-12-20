import socket
import keyboard

HOST, PORT = '127.0.0.1', 4455
addr = (HOST, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(addr)

    while True:
        pressed_key = client.recv(SIZE).decode(FORMAT)
        client.send("key reccived".encode(FORMAT))
        keyboard.press(pressed_key)
        print(pressed_key)

        



if __name__ == "__main__":
    main()
