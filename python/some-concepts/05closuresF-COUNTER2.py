def add(a, b):
    return a + b

def mult(a, b):
    return a * b

########################

d = {} # im going store the function name and how many times we called them 
def counter(fn): 
    counter = 0
    def inner(*args, **kwargs): 
        nonlocal counter
        counter += 1
        d[fn.__name__] = counter # {'add': 2} ... {'add': 2, 'mult': 1} and so on..
        return fn(*args, **kwargs) 
    return inner

f = counter(add)
print(f(1, 2)) 
print(f(5, 5))

mult = counter(mult) 
print(mult(3, 5)) 

print(d) # printing the dict object
         # which contains the function names and the respective number of times we called them
