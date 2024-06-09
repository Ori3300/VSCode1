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
    

def for_loop_task():
    num_list = [1, 2, 3, 4, 5, 6]
    sum = 0
    for num in num_list:
        if num%2 == 0:
            sum += num**2
    print(sum)

for_loop_task()