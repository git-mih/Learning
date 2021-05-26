# Class decorator
class MyClass:
    def __init__(self, a, b): # acts like the decorator factory
        self.a = a
        self.b = b

    def __call__(self, fn):   # __call__(fn) is the decorator itself
        def wrapper(*args, **kwargs):
            print('a={0}, b={1}'.format(self.a, self.b))
            return fn(*args, **kwargs)
        return wrapper

obj = MyClass(10, 20)  # obj is callable, cause we declared the __call__(fn)
def func1():
    print('func running')
func1 = obj(func1)      # obj.__call__(self, fn)
# func1()

# We could also use the syntax sugar:
@MyClass(10, 20)  # MyClass(a,b) will return an callable obj, the decorator itself
def func2():      # func2 = MyClass(10,20)(func_2) 
    print('func2 running')
# func2() 