def add(a, b):
    return a + b

def mult(a, b):
    return a * b

########################

def counter(fn, d):  # expecting a function object and a dictionary
    counter = 0
    def inner(*args, **kwargs): 
        nonlocal counter
        counter += 1
        d[fn.__name__] = counter # storing the name of the function inside the dict as key and the counter as value 
        return fn(*args, **kwargs) 
    return inner
d1 = {} # dict to store how many times we called f()/ add()
f = counter(add, d1) # passing the dict object to the function
print(f(1, 2)) 
print(f(5, 5))
print(d1)

d2 = {} # dict to store how many times we called mult()
mult = counter(mult, d2) 
print(mult(3, 5)) 
print(d2)

