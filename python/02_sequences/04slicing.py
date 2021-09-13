# Slicing:

# Slicing relies on indexing, when we talk about slice we are talking about the indices of the
# elements in a sequence. meaning that, it will only work with sequence types.
#     - sequence[start:stop[:stride]] -> sequence

# altough we usually slice sequences using the conventional notation:
'abcde'[0:2]    # abc
'abcde'[None:2] # abc

# stride:
'abcde'[0:5:2]  # ace

# reversing:
'abcde'[::-1]   # edcba



# the slice definition is actually an object with attributes:
s = slice(0, 2) # <class 'slice'>
dir(s)          # [..., 'indices', 'start', 'step', 'stop']

# we can use that slice object inside the [ ] as well:
[10, 20, 30][s] # 10, 20

# one shot and stride:
'abcdefg'[slice(None, 5, 2)] # ace

# the attribute 'indices' is an method that returns an tuple containing (start, stop, step).
# but that method allow us to specify the length of the sequence that we want to slice:
s = slice(0, 100) # slice(0, 100, None)

s.indices         # <built-in method indices of slice object at 0x001>

# specifying the lenght that we want to slice:
print(s.indices(5))  # (0, 5, 1)
print(s.indices(23)) # (0, 23, 1)


# but, we defined that our slice object will stop at index 100. if we try to pass an length
# greater than that value, we get the stop value:
print(s.indices(999)) # (0, 100, 1)

#__________________________________________________________________________________________________
# range equivalence:

# in fact, any indices defined by a slice can also be defined using the 'range' function.
# but is important to know that, range is only calculated once the length of the sequence 
# that we want to slice is known. for that, we can use the slice attribute 'indices'.


# the 'indices' returned tuple can be used to generate a list of indices using 'range' function. 
# as we know, the 'range' function receive an start and stop argument, and potentially an step.
#     - range(start, stop [, stride]) -> <class 'range'>

range(0, 2) # range(0, 2)

# we can unpack that tuple when we pass a slice object specifying the length that we want to slice:
range(*slice(0, 100).indices(10)) # range(0, 10)

t = slice(0, 100, 2).indices(10)
list(range(*t)) # [0, 2, 4, 6, 8]

#__________________________________________________________________________________________________
# Assignment using slice objects:

# whenever we use slicing [::], Python is looking for any iterable on the RHS:
# when dealing with slice assignments, 

# delete:
l = [1, 2, 3, 4, 5]  # 0x111 
l[2:] = []  # [1, 2]   0x111

l = [1, 2, 3, 4, 5]  # 0x111 
l[2:] = ''  # [1, 2]   0x111

# insert:
l = [1, 2, 3, 4, 5]         # 0x111
l[2:] = [777] # [1, 2, 777]   0x111

l = [1, 2, 3, 4, 5]  # 0x111
l[0:2] = ['a', 'b']  # 0x111 
#        ['a', 'b', 3, 4, 5]
