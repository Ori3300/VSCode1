def binary_task_1():
    number = int(input("enter number: "))
    size = int(input("enter zize: "))

    #להפוך את המספר הערוני לייצוג בינארי
    binary = ""
    while size > 0:
        if 2 ** (size-1) <= number:
            number -= 2 ** (size-1)
            binary += "1"
        else:
            binary += "0"
        size -= 1
    print("binary: " + binary)

    #פעולת המשלים לשתיים
    #הפיכת הסיביות
    binary_not = ""
    for i in range(len(binary)):
        if binary[i] == "0":
            binary_not += "1"
        else:
            binary_not += "0"
    print("not: " +binary_not)

    #הוספת 1
    integer_number = int(binary_not, 2)  # Convert binary to integer
    incremented_number = integer_number + 1  # Add 1
    binary_result = bin(incremented_number)[2:]  # Convert back to binary and remove '0b' prefix
    print("plus 1: " +binary_result)

    #הפיכת המספר הבינארי לעשרוני
    int_binary = int(binary_result, 2)
    print("negative number: " , int_binary)
    



    



binary_task_1()
