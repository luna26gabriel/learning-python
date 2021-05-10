import threading
import time

def eat():
    time.sleep(3)
    print("Eat")
def coffee():
    time.sleep(1)
    print("Coffee")
def study():
    time.sleep(2)
    print("Study")

x = threading.Thread(target=eat, args=())
x.start()
y = threading.Thread(target=coffee, args=())
y.start()
z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

# eat()
# coffee()
# study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())