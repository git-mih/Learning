import time

t0 = time.perf_counter()
def f1():
    time.sleep(1.5)
f1()
t1 = time.perf_counter()
print(t1-t0)

