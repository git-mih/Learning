def timer(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start_time = perf_counter()
        result = fn(*args, **kwargs) # calling fn() 
        elapsed_time = perf_counter() - start_time

        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for k, v in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)

        print('{0}({1}) -> {2}. And took {3:.6f}s to run.'.format(fn.__name__, args_str, result, elapsed_time))
        return result

    return inner

@timer
def fibonacci_with_loop(n):
    a = 1
    b = 1
    for i in range(3, n+1):
        a, b = b, a + b
    return b
