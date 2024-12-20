import hashlib

def main():
    Hash_recived = "3cc6520a6890b92fb55a6b3d657fd1f6"
    for i in range(100000, 999999):
        i = str(i)
        hash = hashlib.md5()
        hash.update(i.encode())
        hex_digits = hash.hexdigest()
        if  hex_digits == Hash_recived:
            print(f"the password is: {i}")



if __name__ == "__main__":
    main()