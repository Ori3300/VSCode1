from threading import Thread

counter = 0

def Thread1():
    global counter
    for _ in range(100000):
        counter += 1


def Thread2():
    global counter
    for _ in range(100000):
        counter -= 1


t1 = Thread(target=Thread1)
t2 = Thread(target=Thread2)

t1.start()
t2.start()

t1.join()
t2.join()

print(counter)