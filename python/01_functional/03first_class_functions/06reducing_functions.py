# Reducing functions:        also called accumulators, aggregators and folding functions.

# functions that recombine an iterable object recursively, ending up with a single value.


# for exemple, finding the maximum value present in an iterable object:
max([3, 7, 4]) # 7

# essentially:
get_max = lambda x, y: x if x > y else y

def max_(iterable):
    result = iterable[0]   # result=3  //  result=7
    for e in iterable[1:]: # [7, 4]
        result = get_max(result, e) # 3 > 7? result=7  //  7 > 4? result=7
    return result

max_([3, 7, 4]) # 7

# once the iterable object get exhausted, the reducing function returns the value.



# writing our custom reduce function that works with sequence objects:
def reduce_(fn, sequence):
    result = sequence[0]
    for e in sequence[1:]:
        result = fn(result, e)
    return result

# getting max value present in the iterable object:
get_max = lambda x, y: x if x > y else y
reduce_(get_max, [1, 2, 3])  # 3
reduce_(lambda x, y: x if x < y else y, 'python')  # h

# getting min value present in the iterable object:
get_min = lambda x, y: x if x < y else y
reduce_(get_min, [1, 2, 3])  # 1

# getting the sum of all iterable elements:
add = lambda x, y: x + y
reduce_(add, [1, 2, 3, 4])  # 10

# subtracting all iterable elements:
sub = lambda x, y: x - y
reduce_(sub, [10, 5, 3])  # 2


#______________________________________________________________________________________________________
# Functools module and Python built-in reduce function:

# reducing functions are really important. and for that, Python provides a built-in module that 
# contains an robust reduce function that works with any iterable object.

# reduce(fn, iterable, [initializer]) -> single value

# iterable: an iterable object of any type that will be called recursevely till it get exhausted.
# fn:  an function that receives 2 arguments and returns a single value whenever it exhaust the
#      iterable object.
# initializer: provides a default initial value to the iterable object.

# essentially, the function will get the first 2 elements of the iterable object:
# l = [1, 2, 3, 4]
# fn(l[0], l[1]) -> <new_value>
#     1     2

# the reduce will pass that returned single value as the first argument to the next call:
# fn(<new_value>, l[2]) -> <new_value>
#                  3

# fn(<new_value>, l[3]) -> <final_value>
#                  4


from functools import reduce

# works like our custom reduce_ function:
reduce(lambda x, y: x if x > y else y, [3, 2, 6]) # 6
reduce(lambda x, y: x if x + y else y, [3, 2, 6]) # 11
reduce(lambda x, y: x if x < y else y, 'python')  # h


# any iterable objects, not just sequences like our custom reduce_:
reduce(lambda x, y: x if x < y else y, {3, 2, 6}) # 6

# concatenating strings together from an iterable, like the join function does:
reduce(lambda a, b: f'{a} {b}', ('just', 'do', 'it')) # just do it

# essentially:
# a='just', b='do'  //  a='just do', b='it'
#     'just do'              just do it



# the 3rd optional argument is often used to provide some kind of default initial value in cases
# that we have an empty iterable object, like:
# reduce(lambda x, y: x + y, []))  TypeError: reduce() of empty sequence with no initial value.


# to avoid that, we pass in the initializer argument specifying some initial value:
reduce(lambda x, y: x + y, [], 100) # 100

# if the iterable object isnt empty, we will essentially put that initializer value in front of 
# the iterable object:
reduce(lambda x, y: x + y, [1, 2, 3], 100) # 106
# essentially:  reduce(fn, [100, 1, 2, 3])


#______________________________________________________________________________________________________
# Built-in reducing functions:

# Python provides several commom reducing functions, like: join, min, max, sum, any, all, ...
min([5, 8, 6, 10, 9]) # 5
max([5, 8, 6, 10, 9]) # 10
sum([5, 8, 6, 10, 9]) # 38


# any and all are related to boolean expressions, they look up the Truthy value of each element
# and return either True or False.

# any:  returns True iff at least one iterable element is Truthy. otherwise, it returns False.
any([0, '', None, 42]) # True

# all:  returns True iff all elements inside the given iterable are Truthy.
all([1, 2, 3])         # True
all([0, '', None, 42]) # False



# using reduce to reproduce the built-in `any` function:
reduce(lambda a, b: bool(a) or bool(b), [0, '', None, 42])  # True

# essentially:
# a=0, b=''  //  a=False, b=None  //  a=False, b=42
#   False             False                True

# we can do the same thing with the built-in `all` as well:
reduce(lambda a, b: bool(a) and bool(b), [1, 2, 3])         # True
reduce(lambda a, b: bool(a) and bool(b), [0, '', None, 42]) # False
