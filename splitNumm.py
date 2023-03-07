# import threading
# import time
# import sys
#
# def hello():
#     for i in range(0,10):
#         print(i)
# def hi():
#     for i in range(10,20):
#         print(i)
# t1=threading.Thread(target=hello)
# t2=threading.Thread(target=hi)
# t1.start()
# t2.start()
# print(threading.enumerate())
# print(threading.active_count())
# sys.exit("Executed Successfully")

try:
    print(1/0)
except:
    raise Exception("Hello")
