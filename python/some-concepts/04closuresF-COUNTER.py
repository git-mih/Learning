def add(a, b):
    return a + b

def mult(a, b):
    return a * b

########################

def counter(fn): # expecting a function object
    counter = 0
    def inner(*args, **kwargs): # add(a,b) or mult(a,b)
        nonlocal counter
        counter += 1
        print(f"{fn.__name__} has been called {counter} times:", end=' ')
        return fn(*args, **kwargs) # calling add(a,b) or mult(a,b) after perform the counting functionality
    return inner

f = counter(add)
print(f(1, 2)) # add has been called 1 time(s)  3
print(f(5, 5)) # add has been called 2 time(s)  10

mult = counter(mult) # masking the old mult function, like decorators do. now we have the counting mechanic
print(mult(3, 5)) # mult has been called 1 time(s)  15
print(mult(2, 4)) # mult has been called 2 time(s)  8
