# map, filter, zip and list comprehension as alternative

# High order function:
# are functions that takes a function object as parameter and/or returns a function object as value. 
# the built-in `sorted` function is a high order function for exemple.

# but we also have the built-in map and filter functions.


# is important to know that, list comprehensions and generator expressions can do the same thing
# that map and filter does essentially. list comprehensions and generator expressions are modern
# alternatives to these high order functions.

#_______________________________________________________________________________________________________
# map function:  map(fn, *iterables) -> iterator object

# *iterables: an variable number of iterable objects.
# fn: some function that takes as many arguments as iterable objects that we passed in.

# that function will be called for each iterable element. 
# if we pass more than one iterable object, the function will be applied in parallel for each 
# iterable element.


# map returns an iterator object that yield mapped elements of the iterable object:
map(lambda e: e**2 , [2, 3, 4])  # <map object at 0x000001>

# exhausting that map object into a list object:
list(map(lambda e: e**2 , [2, 3, 4])) # [4, 9, 16]

# we passed a single iterable. therefore, our function requires just single argument.
# that function will be called for each element of that iterable. 


# all elements present in the iterable object will be mapped essentially, 
# and they will be yielded from that iterator object, whenever we request it:
e = map(lambda e: e**2, [2, 3, 4])
next(e) # 4
next(e) # 9
next(e) # 16


# we can actually pass any number of iterables and our function will map them in parallel:
l1 = [1, 2, 3]
l2 = [4, 5, 6]

# but for that, our function needs to receive 2 arguments, cause we are going to get 1 element
# of each iterable in parallel:
def add(x, y): 
    # l1[0], l2[0]  //  l1[1], l2[1]  //  l1[2], l2[2]
    return x + y

list(map(add, l1, l2)) # [5, 7, 9]

# it will basicly takes one element of each iterable and pass these elements to the add function:
# x=l1[0], y=l2[0] // l1[1], l2[1] // l1[2], l2[2]
#     1  +  4           2  +  5         3  +  6
#        5                 7               9


# the iterator will stop yielding values as soon as one of the iterables get exhausted. 
# it means that, we can map iterable objects that have unequal length.

# it will keep mapping till some iterable get exhausted:
list(map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6, 7, 8, 9, 10])) # [5, 7, 9]

#_______________________________________________________________________________________________________
# filter function:  filter(fn, iterable) -> iterator object

# iterable: single iterable that we want to filter based on some condition.
# fn: the function that takes a single argument and get called for each element of the iterable.

# if the function returns True, it yields the element. otherwise, discard the current element:
list(filter(lambda e: e % 2 == 0, [0, 1, 2, 3, 4])) # [0, 2, 4]

# essentially:
e = filter(lambda e: e % 2 == 0, [0, 1, 2, 3, 4]) # <filter object at 0x000001>
next(e)   # 0
# next(e) # Falsy
next(e)   # 2
# next(e) # Falsy
next(e)   # 4


# the function can be set to None, it will yield elements of the iterable based on its Truthiness:
list(filter(None, [0, 1, 2, '', 3])) # [1, 2, 3]

#_______________________________________________________________________________________________________
# zip function:  zip(*iterables) -> iterator object

# zip takes multiple iterables and returns a iterator object:
zip([1, 2, 3, 4], [10, 20, 30, 40]) # <zip object at 0x000001>

# it will basicly combine each element of the iterables that we passed in:
list(zip([1, 2, 3, 4], [10, 20, 30, 40])) # [(1, 10), (2, 20), (3, 30), (4, 40)]


# the returned iterator object yields a tuple containing the firsts elements of each iterable that
# were passed in, and the seconds, thirds, and so on:
e = zip([1, 2, 3, 4], [10, 20, 30, 40])
next(e) # (1, 10)
next(e) # (2, 20)
next(e) # (3, 30)
next(e) # (4, 40)


# it will stop at the shortest iterable as well:
l1 = range(3)
l2 = 'fabio'
l3 = [8, 9, 10, 11, 12, 13]

list(zip(l1, l2, l3))  # [(0, 'f', 8), (1, 'a', 9), (2, 'b', 10)]


# the zip function isnt a high order function, but its really useful in combination with 
# high order functions, list comprehensions and generator expressions.

#_______________________________________________________________________________________________________
# List comprehension:   [<expression> for <var_name> in <iterable> [condition]] -> list object

# is important to note that, it expect just a single iterable object. if we want to apply the 
# list comprehension to many iterables at the same time, we require to merge them into a single 
# iterable object. for that we can use the built-in zip function.


# alternative to the map function (single iterable):
[e**2 for e in [2, 3, 4]]  # [4, 9, 16]

# it will add each iterable element to that symbol `e` and the output of that expression will be 
# appended to the final list object:
# e=2   //  e=3   //  e=4
# 2**2      3**3      4**4
#  4         9         16

# alternative to the map function (multiple iterables):
l1 = [1, 2, 3]
l2 = [4, 5, 6]

[e1+e2 for e1, e2 in zip(l1, l2)] # [5, 7, 9]

# essentially:
zip(l1, l2) # <zip object at 0x000001> that is going to yield:  (1, 4), (2, 5), (3, 6)
# it is basicly putting each element of the tuple into a symbol: 
# e1=1, e2=4  //  e1=2, e2=5  //  e1=3, e2=6
#    1 + 4           2 + 5           3 + 6
#      5               7               9



# alternative to the filter function:
[e for e in [0, 1, 2, '', 3] if e]  # [1, 2, 3]

# we are essentially applying that condition for each iterable element. 
# only elements that satisfied that condition are going to be appended to the list object.

# another exemple:
[e for e in [1, 2, 3, 4] if e % 2 == 0]  # [2, 4]

# essentially:
# 1 % 2 == 1 Falsy
# 2 % 2 == 0 Truthy  [].append(2)
# 3 % 2 == 1 Falsy
# 4 % 2 == 0 Truthy  [2].append(4)



# combining map and filter:
list(filter(lambda x: x <= 25, map(lambda x: x**2, range(1, 10))))      # [1, 4, 9, 16, 25]

# essentially:
list(filter(lambda x: x <= 25, [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])) # [1, 4, 9, 16, 25]

# equivalent by using list comprehension:
[e**2 for e in range(1, 10) if e**2 <= 25]  # [1, 4, 9, 16, 25]
