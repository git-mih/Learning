# The operator module

# this module provide a set of functions corresponding to the intrinsic operators of Python.

# but these functions are just for convenience, we can always use our own custom functions to perform
# commum operationrs instead.

import operator

# instead of writing the following expression:
3 + 7 # 10

# we could do the same by using a functional approach:
operator.add(3, 7) # 10

#______________________________________________________________________________________________________
# in scenarios like when we were passing function objects as arguments to high order functions,
# they are very useful.

# we dont require to write our own functions to perform these commum operations:
from functools import reduce

# we were essentially doing it before:
reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]) # 15

# but we can use these built-in functions to do the same thing instead:
operator.add   # <built-in function add> -> int object.

reduce(operator.add, [1, 2, 3, 4, 5]) # 15


# object comparison functions:
operator.lt(10, 3) # False   (10 < 3)


# it also provides an functional identity operator equivalent to `is` to perform identity test:
operator.is_(10, 10) # True  (10 is 10)


# we can also see at the truthness of given object:
operator.truth([1, 2]) # True
operator.truth([])     # False

#______________________________________________________________________________________________________
# operations that works with sequence objects:

# we can get an element based on its index, but using the functional approach:   
#      operator.getitem(seq, idx) -> seq[idx]

operator.getitem([1, 2, 3], 2) # 3

# essentially:
[1, 2, 3][2] # 3


# we can also perform set and remove operations:
#      operator.setitem(seq, index, value) -> seq[index] = value
l = [1, 2, 3]
operator.setitem(l, 1, 'pypy') # l[1] = 'pypy'
l # [1, 'pypy', 3]

#      operator.delitem(seq, index) -> del seq[index]
l = [1, 2, 3]
operator.delitem(l, 0) # del l[0]
l # [2, 3]



# if operator.getitem returns some function object:
operator.getitem([1, 2, lambda: 'ABC'], 2)    # <function <lambda> at 0x000001>
operator.getitem([1, 2, lambda: 'ABC'], 2)()  # ABC


#___________________________________________________________________________________________________
# the operator module also provide tools for generalized attribute and element lookups. 
# they are useful for making fast field extractors as arguments for map(), sorted() or any other 
# high order functions that expect a function as argument:



# we use a partial function that we only require to specify the index to get the element that
# correspond to the given index:
#      operator.itemgetter(*index) -> partial function object -> f[index]

# if multiple arguments are specified, returns a tuple object:  (f[index], f[index], ...)

f = operator.itemgetter(2)
callable(f) # True

# that partial function when called, return the element avaiable in that given index (2). 
# but we require to specify the object that it should go and pickup that index:
f([1, 2, 3, 4]) # 3

# essentially:
operator.itemgetter(2)([1, 2, 3, 4]) # 3   [1, 2, 3, 4][2]

# our partial function will works with any object that is indexable and have that pre-defined 
# index (2):
f('Python')  # t

# essentially:
operator.itemgetter(2)('ABCDEF') # C   'ABCDEF'[2] 


# we can also specify more than 1 argument value when using itemgetter:
operator.itemgetter(0, 2, 4)([4, 2, 8, 77, 34]) # (4, 8, 34)
operator.itemgetter(0, 2, 4)('ABCDEF') # ('A', 'C', 'E')


# it works with mapping object as well. they just require to have the __getitem__ method defined:
hasattr({'name': 10}, '__getitem__')  # True

operator.itemgetter('name')({'name': 'Python'}) # Python



# specific function to deal with attributes, where we can lookup inside some object by searching 
# for an specified attribute name:
#      operator.attrgetter(*attributes) -> partial function -> f.attr

# if more than one attribute is requested, returns a tuple of attributes: (f.attr, f.attr, ...)

class Person:
    # creating 4 attributes: name, age, address and say_hello.
    def __init__(self):
        self.name = 'Fabio'
        self.age = 26
        self.address = {'city': 'POA'}

    def say_hello(self):
        return 'hello!'

p = Person()  # <__main__.Person object at 0x000001>


# it basicly takes an string as argument now:
operator.attrgetter('name')(p)  # Fabio

# its essentially doing it:
p.name # Fabio

# getting more tha one attribute:
operator.attrgetter('age', 'address')(p) # (26, {'city': 'POA'})


# we can also get that method (callable attribute):
operator.attrgetter('say_hello')(p) # <bound method Person.say_hello of <Person object at 0x01>>
operator.attrgetter('say_hello')(p)() # hello!

# essentially:
p.say_hello() # hello!


# the string class provides the callable attribute upper which is an method:
f = operator.attrgetter('upper')
f('python') # <built-in method upper of str object at 0x000001>

# require to manually call that method:
f('python')() # PYTHON



# there is a function to deal with methods, where we can call them automatically:
#      operator.methodcaller(attrib, /, *args, **kwargs) -> partial_function.attrib()

operator.methodcaller('say_hello')(p) # hello!   p.say_hello() -> hello!
operator.methodcaller('upper')('ABC') # ABC      'ABC'.upper() -> ABC

# if additional arguments and/or keyword arguments are given, they will be given to the method:
class Person:
    def test(self, a, b, c):
        return a, b, c

p = Person()

operator.methodcaller('test', 10, c=77, b=99)(p)  # (10, 99, 77)  

# essentially:
p.test(10, c=77, b=99) # (10, 99, 77)
