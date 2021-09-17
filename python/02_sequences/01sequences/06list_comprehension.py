# List comprehension

# comprehensions have their own local scope, just like any function.
# we should think of it as being wrapped in a function that is created by Python and returns a
# new list object when get executed.

sq = [i**2 for i in range(10)]

# when that comprehension get compiled:
#     - Python creates a temporary function that will be used to evaluate the comprehension:
def temp():
    l = []
    for i in range(10):
        l.append(i**2)
    return l
# when that comprehension get executed:
#     - Python executes that temporary function (temp), and stores the returned list object in 
#       memory.
#     - makes the symbol 'sq' reference to that list object.

#__________________________________________________________________________________________________
# Comprehension scopes:

# accessing global symbols:
n = 100
#               _________ local symbol
#              /           ,_______ enclosing scope (global scope)
print([item**2 for item in range(n)]) # [0, 1, 4, 9, 16, 25, ..., 9801]


# accessing nonlocal symbols:                  _____ nonlocal symbol
def f(n): #                         /
    sq = [item**2 for item in range(n)]     # Closure


# nested comprehension (nonlocal scope):
[[i*j for j in range(5)] for i in range(5)] # Closure
# [
#   [0, 0, 0, 0, 0], 
#   [0, 1, 2, 3, 4], 
#   [0, 2, 4, 6, 8], 
#   [0, 3, 6, 9, 12], 
#   [0, 4, 8, 12, 16]
# ]

#__________________________________________________________________________________________________
# conditions:
[i for i in range(100) if i % 2 == 0] # [0, 2, 4, 6, 8, ...]
