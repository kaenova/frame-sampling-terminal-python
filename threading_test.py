from threading import Thread
import time

data = []

def worker1(data:list):
    while True:
        time.sleep(1)
        print("dari 1", data)
        
def worker2(data:list):
    while True:
        time.sleep(1.5)
        print("dari 2", data)
        
        
t1 = Thread(target=worker1, args=(data,))
t2 = Thread(target=worker2, args=(data,))

t1.start()
t2.start()
while True:
    time.sleep(0.3)
    i = 0
    data.append(i)
    i+=1