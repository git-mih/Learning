# Sequence types:

# when talking about sequences, we have the concept of 1st, 2nd, 3rd element, and so on.
# we can refer to any item inside a sequence by using its index number, for exemple:
l = [1, 2, 3, 4]
l[0]  # 1

s = 'abcde'
s[3]  # d

r = range(4)
r[-1] # 3

#______________________________________________________________________________________________
# Built-in sequence types:

# mutable: 
# - lists, bytearrays

# immutables:
# - strings, tuples, range, bytes

#______________________________________________________________________________________________
# iterable objects:

# an iterable is essentially just a container object where we can list out all elements that is
# avaiable inside that container. we can basicly access its elements one by one.

# it means that, any sequence type is an iterable object essentially:
for e in [1, 2, 3]:
    pass  
# 1
# 2
# 3

for e in 'abc':
    pass
# a
# b
# c

for e in range(3):
    pass
# 0
# 1
# 2


# but an iterable isnt necessaraly an sequence type. for exemple, sets arent sequences, but we 
# can iterate over it to access all elements, one by one:
for e in {1, 2, 3}:
    pass
# 3
# 1
# 2

# iterables are more general.

#______________________________________________________________________________________________
# standard sequence methods:

# built-in mutable and immutable sequence types, supports the following methods:

# membership (__contains__ method):
1 in [1, 'a', True] # True
'z' not in 'abcde'  # True


# length (__len__ method):
len([1, 2, 3])  # 3
len('aeiou')    # 5

# also applicable to mapping objects:
len({5, 3, 1, 7})     # 4
len({'a': 1, 'b': 2}) # 2


# min/max  (comparasion should be implemented to support their types: __gt__ method, etc...):
min([1, 2, 3, 4])     # 1
max([1, 2, 3, 4])     # 4

min(['a', 'b', 'c'])  # a
max(['a', 'b', 'c'])  # c
# min(['a', 1, 2, 3])    TypeError: '<' not supported between instances of 'int' and 'str'


# range objects are more restrictive, we cant concatenate them. but we can use methods like 
# min/max, in/not in. not being as efficient dealing with range objects though:
min(range(5))  # 0
max(range(5))  # 4
3 in range(5)  # True


# index method (returns the first occurrence, start index included):
# we can enumerate any iterable by using the built-in function enumerate: 
#     enumerate(seq) -> iterator
s = 'gnu is not unix'
list(enumerate(s))    # list(<enumerate object at 0x01>)
# [
#  (0, 'g'), 
#  (1, 'n'), 
#  (2, 'u'), 
#  (3, ' '), 
#  (4, 'i'), 
#  (5, 's'), 
#  (6, ' '), 
#  (7, 'n'), 
#  (8, 'o'), 
#  (9, 't'), 
#  (10, ' '), 
#  (11, 'u'), 
#  (12, 'n'), 
#  (13, 'i'), 
#  (14, 'x')
# ]

s.index('n')     # 1
s.index('n', 2)  # 7


# slicing:
# copying a sequence (creates a new sequence object):
l1 = [1, 2] # [1, 2] 0x01
l2 = l1[:]  # [1, 2] 0x02

# reversing:
[1, 2, 3][::-1] # [3, 2, 1]
'abc'[::-1]     # cba



# hashing:
# immutable sequence types may support hashing as well, but they can not contain mutable objects.
#     hash(sequence) -> int   (sequence must be immutable)
hash('abcd')      # 5937197789390855713
# hash([1, 2, 3])   TypeError: unhashable type: 'list'

#______________________________________________________________________________________________
# Sequence concatenation and Shallow copies:

[1, 2] + [1, 2]   # [1, 2, 1, 2]
(1, 2) + (1, 2)   # (1, 2, 1, 2)
'abc' + 'abc'     # abcabc

[1, 2] * 2        # [1, 2, 1, 2]
'abc' * 2         # abcabc
2 * 'abc'         # abcabc

# we cant concatenate two different sequence objects that arent of the same type:
# [1, 2] + 'abc'            TypeError: can only concatenate list (not "str") to list
# 'abc' + ['d', 'e', 'f']   TypeError: can only concatenate str (not "list") to str
list('abc') + ['d', 'e']  # ['a', 'b', 'c', 'd', 'e']


# if we want to make a sequence into a string, we use the join method: 
#     str.join(sequence) -> str  (sequence needs to be a sequence of strings, ['str'] or 'str')
''.join(['a', 'b', 'c', 'd', 'e'])   # abcde
', '.join(['a', 'b', 'c', 'd', 'e']) # a, b, c, d, e
' - '.join('abcde')                  # a - b - c - d - e
# ''.join([1, 2, 3])    TypeError: sequence item 0: expected str instance, int found



# whenever we concatenate sequence types, we are essentially creating a new sequence object:
s1 = [1, 2]  # [1, 2]       0x001
s2 = s1 + s1 # [1, 2, 1, 2] 0x002

s1 = 'abc'   # 'abc'    0x001
s2 = s1 + s1 # 'abcabc' 0x002

s1 = ['abc'] # ['abc']        0x001
s2 = s1 + s1 # ['abc', 'abc'] 0x002


# concatenating with * operator (repetition) approach:
s1 = [1, 2]
s2 = s1 * 2  # [1, 2, 1, 2]

s1 = 'abc'
s2 = s1 * 2  # 'abcabc'

s1 = ['abc']
s2 = s1 * 2  # ['abc', 'abc']



# beware of concatenating sequences that contain mutable objects:
s1 = [[0, 0]] # [[0, 0]]         0x1
s2 = s1 + s1  # [[0, 0], [0, 0]] 0x2

# Shallow copies:
s1[0] # 0x001 
s2[0] # 0x001 
s2[1] # 0x001 

s2[0][0] = 999

s1 # [[999, 0]]            0x1
s2 # [[999, 0], [999, 0]]  0x2


# repetition:
s1 = [[0, 0]]
s2 = s1 * 2  # [[0, 0], [0, 0]]

s2[1][1] = 777
s1 # [[0, 777]]
s2 # [[0, 777], [0, 777]]
