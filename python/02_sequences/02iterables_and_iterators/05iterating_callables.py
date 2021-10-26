# iterating over the return values of a callable object

# Consider a callable that provides a countdown value for each call:
# countdown() -> 3
# countdown() -> 2
# countdown() -> 1
# countdown() -> 0

# We now want to run a loop that will call that function until the value 0 is reached.
# we could certainly do that using a loop and testing the value to break out of the loop, like:
# while True:
#     val = countdown()
#     if val = 0:   # 0 is our Sentinel value in this case.
#         break
#     else:
#         print(val) # 3, 2, 1


# we can take a different approach, by using iterators and making it more generic to be able to
# work with any callable object.

# we require to make an iterator that knows two things:
#   The callable that needs to be called.
#   A value (SENTINEL) that will result in a StopIteration if the callable returns that value.

# Once the sentinel value is reached, we should Raise the StopIteration exception and exhaust the
# iterator immediately.

# Implementing as follow:
# when next() gets called, we call the callable object and get the result.
# if the result of that call is equal to the sentinel value, we raise an StopIteration and exhaust
# the iterator object. Otherwise, we just return that result.

# But we should care about infinite loops, if the callable never returns the sentinel value, it
# would be a issue, we have to make sure that, the callable object will result in the sentinel value
# eventually.

def counter():
    i = 0
    def inc():
        nonlocal i
        i += 1
        return i
    return inc

class CallableIterator:
    def __init__(self, _callable, sentinel):
        self._callable = _callable
        self.sentinel = sentinel
        self.is_consumed = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_consumed:
            raise StopIteration
        else:
            result = self._callable()
            if result == self.sentinel:
                self.is_consumed = True # Exhausting the iterator
                raise StopIteration
            else:
                return result

cnt = counter()
cnt_iter = CallableIterator(cnt, 5)

for _ in range(10): print(next(cnt_iter))
# 1
# 2
# 3
# 4
# StopIteration
next(cnt_iter) # StopIteration

cnt_iter = CallableIterator(cnt, 3)
for c in cnt_iter: print(c)
# 0
# 1
# 2
next(cnt_iter) # StopIteration

#____________________________________________________________________________________________________-
# The iter() function have two forms, the first one that we saw, and it also have another one that
# we can specify an Sentinel value.

# iter(iterable) -> iterator
# iter(callable, sentinel) -> iterator

# This extended form of the iter() function is exactly the same, but this one can raise an StopIteration
# exception once the callable results in the sentinel value as well.

cnt = counter()
cnt_iter = iter(cnt, 3)
for c in cnt_iter: print(c)
# 0
# 1
# 2
next(cnt_iter) # StopIteration
