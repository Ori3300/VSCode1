import socket
import os
import shutil

HOST, PORT = "127.0.0.1", 4455
ADDR = (HOST, PORT)
FORMAT = "utf-8"
SIZE = 1024


def store_in_folder(file_path, destination_folder):
    shutil.move(file_path, destination_folder) 
    



def main():
    print("[STARTING] server is starting.")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print("[LISTENING] serveris listening.")
    while True:
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")
        act = conn.recv(SIZE).decode(FORMAT)
        print("[RECV] act recived")
        conn.send("act recived".encode(FORMAT))


        if act == "upload":
            file_name = conn.recv(SIZE).decode(FORMAT)
            print("[RECV] Filename recived.")
            conn.send("Filename recived successfuly".encode(FORMAT))
            file_folder_path = f"C:\\Users\\user\\Desktop\\VSCode\\uploadDownload\\storage\\{file_name}"

            if os.path.isfile(file_folder_path):
                print("[MESSAGE] file has already been stored.")
                conn.send("False".encode(FORMAT))
            else: 
                conn.send("True".encode(FORMAT))
                data = conn.recv(SIZE).decode(FORMAT)
                print("[RECV] File data recived.")
                with open(file_name, 'w') as file:
                    file.write(data)
                
                conn.send("File data recived successfuly".encode(FORMAT))

                destination_folder = "C:\\Users\\user\\Desktop\\VSCode\\uploadDownload\\storage"
                store_in_folder(file_name, destination_folder)

                
        else:
            file_name = conn.recv(SIZE).decode(FORMAT)
            print("[RECV] file name recived.")
            conn.send("file name recived successfuly".encode(FORMAT))

            if os.path.exists(file_name):
                print("[MESSAGE] file exist.")
                conn.send("True".encode(FORMAT))
                file_path = f"C:\\Users\\user\\Desktop\\VSCode\\uploadDownload\\storage\\{file_name}"

                with open(file_path, 'r') as file:
                    data = file.read()
                
                conn.send(data.encode(FORMAT))
            else:
                print("[MESSAGE] file does not exist.")
                conn.send("False".encode(FORMAT))

                



        
            


    
    


    

        

        

        

if __name__ == "__main__":
    main()

