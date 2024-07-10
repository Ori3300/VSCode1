import socket

HOST, PORT = '127.0.0.1', 4455
addr = (HOST, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(addr)
    
    act = input("upload or download? ")
    client.send(act.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    if act == "upload":
        file_path = input("enter the file path:")


        with open(file_path, 'r') as file:
            data = file.read()

        client.send("desktop.txt".encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {msg}")

        IsExist = client.recv(SIZE).decode(FORMAT)
        client.send("IsExist Recive".encode(FORMAT))

        if IsExist == "True":
            msg = client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER]: {msg}")

            client.send(data.encode(FORMAT))

            msg = client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER]: {msg}")
        else:
            print("file has already been stored")



    else:
        file_name = input("enter file name: ")
        client.send(file_name.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"[SERVER]: {msg}")

        IsExist = client.recv(SIZE).decode(FORMAT)
        client.send("IsExist Recive".encode(FORMAT))

        if IsExist == "True":
            data = client.recv(SIZE).decode(FORMAT)
            client.send("[CLIENT]: data recived successfuly.".encode(FORMAT))
            print(f"File data recived")

            with open(file_name, 'w') as file:
                file.write(data)
            
            print("file downloaded successfuly.")
        else:
            print("file does not exist")
            





if __name__ == "__main__":
    main()
