# Memoization technique

def memoize(fn): # whatever function we pass here, should have only one argument.
    cache = {}

    def wrapper(n): # any function which take a single parameter, eg: fibonacci, factorial, etc.
        if n not in cache:
            cache[n] = fn(n) 
        return cache[n]
    return wrapper

# without memoization, it would have to calculate the same values again and again
# def fib(n): 
#     print('Calculating fib({0})'.format(n))
#     return 1 if n < 2 else fib(n-1) + fib(n-2)
# fib(10)

@memoize
def fib(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 2 else fib(n-1) + fib(n-2)
fib(10) # try to use fib(9) or 10 again, we get the cached value instead. we dont have to calculate again

print("\nCalculating factorial bellow \n")

@memoize
def fact(n):
    print('Calculating {0}!'.format(n))
    return 1 if n < 2 else n * fact(n-1)
fact(6) # try to use fact(5) or 6 again, we get the cached value instead. we dont have to calculate again