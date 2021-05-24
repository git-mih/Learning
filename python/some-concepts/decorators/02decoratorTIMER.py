def timer(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        elapsed_total = 0
        elapsed_count = 0

        # we have 10 hardcoded here
        for i in range(10): # calling the closure 10 times and getting the avarage time elapsed
            print('Running iteration {0}'.format(i))
            start_time = perf_counter()
            result = fn(*args, **kwargs) 
            end = perf_counter()
            elapsed = end - start_time

            elapsed_total += elapsed
            elapsed_count += 1

        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for k, v in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)

        elapsed_average = elapsed_total / elapsed_count
        print('{0}({1}) -> {2}. And took {3:.6f}s avg time to run.'.format(fn.__name__,
                                                                           args_str, 
                                                                           result, 
                                                                           elapsed_average))
        return result

    return inner

@timer
def fibonacci_with_loop(n):
    a = 1
    b = 1
    for i in range(3, n+1):
        a, b = b, a + b
    return b

fibonacci_with_loop(6)