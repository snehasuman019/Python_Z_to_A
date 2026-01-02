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

# multithreading with arguments
def greet(name):
    print(f"Hello {name}")

t = threading.Thread(target=greet, args=("Sneha",))
t.start()


# multiprocessing 
import multiprocessing
import time

def task():
    print("Task started")
    time.sleep(2)
    print("Task finished")

p1 = multiprocessing.Process(target=task)
p2 = multiprocessing.Process(target=task)

p1.start()
p2.start()

p1.join()
p2.join()

print("Done")
