# Mutable sequences (in-place operations):

# mutating using [ ]:
l = [1, 2, 3, 4, 5]   # 0x0001

l[0] = 777
l # [777, 2, 3, 4, 5] # 0x0001

# mutating with slice: 
l[1:3] = 'abc'  

# shift elements to the right:
l # [777, 'a', 'b', 'c', 4, 5] 0x0001

# mutating with del:
del l[0]
del l[0:3]

l # [4, 5]  0x0001

#________________________________________________________________________________________________
# Mutable sequence types methods (in-place):

# clear:    sequence.clear()
l = [1, 2, 3, 4, 5]    # 0x0001
l.clear()   # l = []   # 0x0001

# append:   sequence.append(element)
l = [1, 2, 3]
l.append(777) # [1, 2, 3, 777]

# extend:   sequence.extend(ITERABLE)
l = [1, 2]
l.extend(['abc'])   # [1, 2, 'a', 'b', 'c']
l.extend({1, 2, 3}) # [1, 2, 'a', 'b', 'c', 3, 1, 2]

# insert:   sequence.insert(index, element)   # shift everything else to right.
l = [1, 2, 3, 4]
l.insert(2, 'abc') # [1, 2, 'abc', 3, 4]

# pop:      sequence.pop() -> sequence[-1]
l = [1, 2, 3]
l.pop       # [1, 2] -> 3

# remove:   sequence.remove(element) -> sequence[-1]   removes 1st occurrence.
l = [1, 2, 3]
l.remove(1) # [2, 3] -> 1

# reverse:  sequence.reverse()
l = [1, 2, 3]
l.reverse   # [3, 2, 1]

#________________________________________________________________________________________________
# list vs tuples:

# tuples are more efficient than lists. Python uses applies an process of recognizing and 
# evaluating constant expressions at compile time rather than computing them at runtime.
# that is a optimization technique called Constant Folding:
from dis import dis
dis(compile('(1, 2, 3, "a")', '<string>', 'eval'))
# 1   0 LOAD_CONST      0 ((1, 2, 3, 'a'))
#     2 RETURN_VALUE

dis(compile('[1, 2, 3, "a"]', '<string>', 'eval'))
# 1   0 BUILD_LIST      0
#     2 LOAD_CONST      0 ((1, 2, 3, 'a'))
#     4 LIST_EXTEND     1
#     6 RETURN_VALUE

dis(compile('[1, [2, 3], "a"]', '<string>', 'eval'))
# 1   0 LOAD_CONST      0 (1)
#     2 LOAD_CONST      1 (2)
#     4 LOAD_CONST      2 (3)
#     6 BUILD_LIST      2
#     8 LOAD_CONST      3 ('a')
#    10 BUILD_LIST      3
#    12 RETURN_VALUE


# Storage diff:
import sys
l = [] 
prev = sys.getsizeof(l)  # 56
print(f'elements: 0  -  bytes: {prev}')
for i in range(255):
    l.append(i)
    new_l = sys.getsizeof(l)
    delta = new_l - prev
    prev = new_l
    # print(f'elements: {i + 1}  -  bytes: {new_l}  -  delta: {delta}')

# elements:  0 -  bytes:  56
# elements:  1 -  bytes:  88  -  delta: 32
# elements:  2 -  bytes:  88  -  delta: 0
# elements:  3 -  bytes:  88  -  delta: 0
# elements:  4 -  bytes:  88  -  delta: 0
# elements:  5 -  bytes: 120  -  delta: 32
# elements:  6 -  bytes: 120  -  delta: 0
# elements:  7 -  bytes: 120  -  delta: 0
# elements:  8 -  bytes: 120  -  delta: 0
# elements:  9 -  bytes: 184  -  delta: 64
# elements: 10 -  bytes: 184  -  delta: 0
# elements: 11 -  bytes: 184  -  delta: 0
# elements: 12 -  bytes: 184  -  delta: 0
# elements: 13 -  bytes: 184  -  delta: 0
# elements: 14 -  bytes: 184  -  delta: 0
# elements: 15 -  bytes: 184  -  delta: 0
# elements: 16 -  bytes: 184  -  delta: 0
# elements: 17 -  bytes: 248  -  delta: 64
#                 .
#                 .                
#                 .

t = ()
prev = sys.getsizeof(t)  # 56
print(f'elements: 0  -  bytes: {prev}')
for i in range(255):
    t = t + (i,)
    new_t = sys.getsizeof(t)
    delta = new_t - prev
    prev = new_t
    print(f'elements: {i + 1}  -  bytes: {new_t}  -  delta: {delta}')

# elements:  0  -  bytes:  40
# elements:  1  -  bytes:  48  -  delta: 8
# elements:  2  -  bytes:  56  -  delta: 8
# elements:  3  -  bytes:  64  -  delta: 8
# elements:  4  -  bytes:  72  -  delta: 8
# elements:  5  -  bytes:  80  -  delta: 8
# elements:  6  -  bytes:  88  -  delta: 8
# elements:  7  -  bytes:  96  -  delta: 8
# elements:  8  -  bytes: 104  -  delta: 8
# elements:  9  -  bytes: 112  -  delta: 8
# elements: 10  -  bytes: 120  -  delta: 8
# elements: 11  -  bytes: 128  -  delta: 8
# elements: 12  -  bytes: 136  -  delta: 8
#                 .
#                 .                
#                 .
