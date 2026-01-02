# multithreading 
import threading
import time

def task():
    print("Task started")
    time.sleep(2)
    print("Task finished")

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()

print("Done")
