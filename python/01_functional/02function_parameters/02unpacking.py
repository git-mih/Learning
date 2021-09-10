# Unpacking iterables

# packed values refers to values that are bundled together in some way. for exemple, tuples,
# lists, strings, sets and dictionaries. in fact, any iterable can be considered a packed value.


# unpacking is the act of splitting iterables/packed values into individual variables:
a, b, c = (1, 2, 3) # 3 elements inside the tuple requires 3 variables to unpack it.

# it was unpacked into individual variables based on the relative position of each element:
a # 1
b # 2
c # 3


# whenever we are calling a function and passing arguments to the function, the function is 
# actually unpacking that tuple into the parameters that was defined in the function:
def f(a, b, c):
    # it will essentially unpack it inside the function namespace:   a, b, c = (1, 2, 3)
    return a, b, c

f(1, 2, 3)  


# unpacking other iterables:
a, b, c = 10, 20, 'hey'
a # 10
b # 20
c # hey

# we can also unpack strings:
a, b, c = 'xyz'
a # x
b # y
c # z


# instead of writing:
a = 10
b = 20

# we could write it this way as well:
a, b = 10, 20


# in fact, unpacking works with any data type that is iterable:
for e in 10, 20, 'hello': # (10, 20, 'hello') unpacking a tuple object
    print(e)
# 10
# 20
# hello

for e in 'xyz': # unpacking a string object
    print(e)
# x
# y
# z


# simple application of unpacking is to swap values of two variables:
a = 10  # 0x0001
b = 20  # 0x0002

# the "traditional" approach, would be do something with a temporary variable like:
tmp = a # temp 0x0003

a = b   # a -> 0x0002
b = tmp # b -> 0x0001


# using unpacking approach:
a, b = b, a

# this works because in Python, the entire RHS is evaluated first. after that, assignments are 
# made to the LHS, essentially:
a, b = (20, 10)
a # 20 # 0x0002
b # 10 # 0x0001



# unpacking dictionaries:
for e in {'key1': 1, 'key2': 2, 'key3': 3}:
    # it will actually iterates through the keys, like:  for e in {'key1', 'key2', 'key3'}
    print(e)
# key1
# key2
# key3

# that means if we are unpack that dictionary, we will actually unpacking only the keys:
a, b, c = {'key1': 1, 'key2': 2, 'key3': 3}
a # key1
b # key2
c # key2


# unpacking sets (there is no ordering in sets):
for e in {'p', 'y', 't', 'h', 'o', 'n'}:
    print(e)
# o
# t
# h
# y
# n
# p

a, b, c = {'a', 'b', 'c'}
a # c
b # a
c # b

#____________________________________________________________________________________________________
# Extended unpacking:

# we dont always want to unpack every single item in an iterable. we may, for exemple, want to 
# unpack the first value and then unpack the remaining values into another variable.

l = [1, 2, 3, 4, 5, 6]

# we can achieve this by using slicing:
a = l[0]  # 1
b = l[1:] # [2, 3, 4, 5, 6]

# but in order to use slice, the object must be an sequence type, it must be indexable.

# we could also make a parallel assignment with unpacking and slicing:
a, b = l[0], l[1:]
a # 1
b # [2, 3, 4, 5, 6]


# but we could also use the * operator to do the same thing:
a, *b = l
a # 1
b # [2, 3, 4, 5, 6]

# apart from cleaner syntax, it also works with any iterable object, not just sequence types.

#________________________________________________________________________________________________
# * operator usage with ordered types:
a, *b = (-10, 5, 2, 100) # unpacking a tuple object.
a # -10
b # [5, 2, 100]      # it will always be unpacked into a list object.

# unpacking strings with * operator:
a, *b = 'xyz'
a # x
b # ['y', 'z']

# also works with any number of elements:
a, b, *c = 1, 2, 3, 4, 5
a # 1
b # 2
c # [3, 4, 5]


# we can also add variables after the * operator:
a, b, *c, d = [1, 2, 3, 4, 5]
a # 1
b # 2
c # [3, 4]
d # 5

# strings as well:
a, *b, c, d = 'python'
a # p
b # ['y', 't', 'h']
c # o
d # n


# the * operator can only be used once in the LHS while unpacking. we cant write something like:
# a, *b, *c = [1, 2, 3, 4, 5]


# we have seen how to use the * operator in the LHS while unpacking:
a, *b, c = {1, 2, 3, 4, 5}

# however, we can also use it in the RHS:
l1 = [1, 2, 3]
l2 = [4, 5, 6]

l = [*l1, *l2] # we are essentially unpacking each individual element of l1 and l2 inside it.
l # [1, 2, 3, 4, 5, 6]

l1 = [1, 2]
l2 = 'xyz'

l = [*l1, *l2] 
l # [1, 2, 'x', 'y', 'z']

#________________________________________________________________________________________________
# * operator usage with unordered types:
# data types such as sets and dictionaries doesnt have ordering guaranteed.
a, *b = {19, -99, 3, 'd'}
a # 19 
b # ['d', 3, -99]


# in practice, we rerely unpack sets directly this way. however, it is useful in a situation where
# we might want to create a single collection containing all items of multiple sets, or keys of
# multiple dictionaries:
d1 = {'p': 1, 'y': 2}
d2 = {'t': 3, 'h':4}
d3 = {'h': 5, 'o': 6, 'n':7} # note that 'h' key is in both, `d2` and `d3`.

d = [*d1, *d2, *d3]  # ['p', 'y', 't', 'h', 'h', 'o', 'n']
d = {*d1, *d2, *d3}  # {'p', 'o', 'y', 'n', 't', 'h'}


# the ** unpacking operator:
# when working with dictionaries we saw that * essentially iterated the keys only. and by using
# the ** operator, we can unpack the key-value pairs of dict objects:
d1 = {'p': 1, 'y': 2}
d2 = {'t': 3, 'h':4}
d3 = {'h': 5, 'o': 6, 'n':7}

d = {**d1, **d2, **d3}  # {'p': 1, 'y': 2, 't': 3, 'h': 5, 'o': 6, 'n': 7}
# note that, `d3` was merged after in the chain, the value of 'h' in `d3` overwrote the first 
# value of 'h' that was in `d2`.


# we can even use it to add key-value pairs from one or more dictionaries into an dict literal:
d = {'a': 1, 'b': 2}

{'a': 777, 'c': 3, **d} # {'a': 1, 'b': 2, 'c': 3}
{**d, 'c': 3, 'a': 777} # {'a': 777, 'b': 2, 'c': 3}

# the ** operator cannot be used in the LHS of an assignment.



# Python supports nested unpacking as well:
a, b, c = [1, 2, [3, 4]]
a # 1
b # 2
c # [3, 4] once we have it, we can keep unpacking:
d, e = c
d # 3
e # 4

# or we could just write that in a single line:
a, b, (c, d) = [1, 2, [3, 4]]
a # 1
b # 2
c # 3
d # 4

# since strings are iterables as well:
a, *b, (c, d, e) = [1, 2, 3, 'xyz']
a # 1
b # [2, 3]
c # x
d # y
e # z

# the * operator can only be used once in the LHS during unpacking, but what about it:
a, *b, (c, *d) = [1, 2, 3, 'python']
a # 1
b # [2, 3]
c # p
d # ython

# although this looks like we are using * twice in the same expression, the 2nd * is actually in
# a nested unpacking, another expression essentially.
