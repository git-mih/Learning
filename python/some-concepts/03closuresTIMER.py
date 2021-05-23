from time import perf_counter, sleep

def timer():
    start = perf_counter()
    def inner():
        nonlocal start
        return perf_counter() - start  # t1 - t0
    return inner

f = timer() # t0 start counting when we create the inner function

sleep(3)

f() # t1 - t0 = time since we instantiated the closure
