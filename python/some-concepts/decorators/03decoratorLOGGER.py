# logging the funcion calls by using decorator

def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def wrapper(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print('{0}: called {1}'.format(run_dt, fn.__name__))
        return result
    return wrapper

@logged
def func_1():
    pass

@logged
def func_2():
    pass

func_1() #   2021-05-25 04:26:59.086143+00:00: called func_1
func_2() #   2021-05-25 04:26:59.086964+00:00: called func_2