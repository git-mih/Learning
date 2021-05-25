#_________________________________________________One

def decorator_1(fn):
    # processing fn. then we return it
    print('DECORATOR!')
    return fn

@decorator_1 # decorator_1(func_1)()
def f1():
    print('func execution...')
# func_1 = decorator_1(func_1)
f1()

#_________________________________________________Two

def decorator_2(fn):
    def wrapper(*args, **kwargs):
        # processing fn and his args/kwargs
        # fn(*args,**kwargs) to call it
        print('DECORATOR!')
        return fn(*args, **kwargs)
    return wrapper

@decorator_2 # decorator_2(func_2)(a, b)
def func_2(a, b):
    pass
# func_2 = decorator_2(func_2)

func_2(1, 2) # calling the wrapper, not the func_2 original func

#_________________________________________________Three

def decorator(F):           # F is func or method without instance
    def wrapper(*args):     # class instance in args[0] for method
        pass                # F(*args) runs func or method
    return wrapper

@decorator
def func(x, y):             # func = decorator(func)
    pass
func(6, 7)                  # Really calls wrapper(6, 7)

class C:
    @decorator
    def method(self, x, y): # method = decorator(method)
        pass                # Rebound to simple function

X = C()
X.method(6, 7)              # Really calls wrapper(X, 6, 7)

#_________________________________________________Four