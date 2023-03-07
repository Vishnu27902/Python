import threading
import time
def Hello():
    for i in range(5):
        print("hi")
        time.sleep(5)
def Hi():
    for i in range(6):
        print("Hello")
        time.sleep(5)
a=threading.Thread(target=Hello)
b=threading.Thread(target=Hi)
a.start()
b.start()
print(threading.active_count())
print(threading.enumerate())
print("Bye")