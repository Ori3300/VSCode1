import random
from threading import Thread

def Culculetor(x,op,y):
    if op == "+":
        print(x + y)
    elif op == "-":
        print(x-y)
    elif op == "*":
        print(x*y)
    elif op == "/":
        print(x/y)
    else:
        print("Unknown Operator")
    

def sum_squre_even_numbers_list():
    num_list = [1, 2, 3, 4, 5, 6]
    sum = 0
    for num in num_list:
        if num%2 == 0:
            sum += num**2
    print(sum)

def guess_number():
    random_number = random.randint(1,100)
    guessed_number = int(input("enter number: "))
    attempts = 0
    while random_number != guessed_number:
        if guessed_number > random_number:
            print("the random number is lower")
        else:
            print("the random number is higher")
        attempts += 1
        guessed_number = int(input("enter number: "))
    
    print(f"congrats in {attempts} attempts")

def convert_C_and_F():
    print("1: celsios to fahrenheit\n")
    print("2: fahrenheit to celsios\n")
    x = int(input("enter 1 or 2: "))
    if x == 1:
        C = int(input("enter the temperture in C: "))
        F = C_to_F(C)
        print("{} celsios is {} fahrenheit".format(C, F))
    else:
        F = int(input("enter the temperture in F: "))
        C = F_to_C(F)
        print("{} fahrenheit is {} celsios".format(F, C))


def C_to_F(C):
    F = C / (5/9)
    F += 32
    return F

def F_to_C(F):
    C = F - 32
    C *= (5/9)
    return C