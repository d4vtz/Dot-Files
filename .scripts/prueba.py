import threading
import time
import sys

def cuenta(n, name):
    count = n
    while count < 10:
        print(count, name)
        count +=1
        time.sleep(2)

t = threading.Thread(target=cuenta, args=(1, '1'))
t2 = threading.Thread(target=cuenta, args=(2, '2'))
t3 = threading.Thread(target=cuenta, args=(3, '3'))

t.start()
t2.start()
t3.start()