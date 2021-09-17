# iterating sequences:

# Python supports a concept of iteration over containers. this is implemented using two distinct 
# methods, __next__ and __iter__. 

# these are used to allow custom classes to support iteration. 
# also, sequence types always support the iteration methods.


# all we need is a collection/container of items and an ideia of getting the next item from that 
# collection/container, no ordering concept required.

class Squares:
    def __init__(self, length):
        self.i = 0
        self.length = length

    # next item:
    def next_(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result

sq = Squares(5)  # <__main__.Squares object at 0x01>

while True:
    try:
        e = sq.next_()
        print(e)
    except StopIteration:
        break
# 0
# 1
# 4
# 9
# 16

#_____________________________________________________________________________________________________
# we can implement the 'next()' function for our custom types by using the __next__ method:

# __next__ method:
# return the next item from the container. if there are no further items, raise the 
# StopIteration exception.


# next(iterator [, default]):
# retrieve the next item from the iterator by calling its __next__ method. 
# if default is given, it is returned if the iterator is exhausted, otherwise StopIteration is raised.

class Squares:
    def __init__(self, length):
        self.i = 0
        self.length = length

    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result

sq = Squares(5)

while True:
    try:
        e = next(sq) # sq.__next__()
        print(e)
    except StopIteration:
        break
# 0
# 1
# 4
# 9
# 16

# next(sq) # StopIteration


# we still have some drawbacks: 
#     - we cannot iterate using for loops, comprehensions, etc.
#     - once the iteration starts, we have no way of re-starting it.
#     - once all items have been iterated (using next) the object becomes exhausted.

#_____________________________________________________________________________________________________
# iterators:

# to be able to do that, we require to implement the iterator protocol. 
# __iter__: return the object (class instance) itself.
# __next__: returns the next element from the container, or raise StopIteration exception.

# if an object is an iterator, we can use it with for loops, comprehensions and so on.

class Squares:
    def __init__(self, length):
        self.i = 0
        self.length = length
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result

sq = Squares(5) # <__main__.Squares object at 0x01>

for item in sq: print(item)
# 0
# 1
# 4
# 9
# 16

# once we have iterated trhough all elements of that iterator, it gets exhausted:
# next(sq)                    # StopIteration
# for item in sq: print(item) # StopIteration
# [i for i in sq]             # StopIteration

# that iterator object (<__main__.Squares object at 0x01>) cannot be "restarted".


# to be able to iterate over again, we would require to instantiate a new iterator object:
sq = Squares(5) # <__main__.Squares object at 0x02>

next(sq)   # 0
next(sq)   # 1
next(sq)   # 4
next(sq)   # 9
next(sq)   # 16
# next(sq) # StopIteration

#_____________________________________________________________________________________________________
# Separating the collection from the iterator:

# instead, we should separate these two, so we can maintain the data of the container in one object,
# ant iterate over a copy of that container/collection object.

# this way, we can throw-away the iterator when it get exhausted, the data we shouldnt.


# the collection is iterable, but the iterator is responsible for iterating over the collection.
# iterable is created once, and the iterator is created every single time that we need to start
# a fresh iteration.

class Cities:
    def __init__(self):
        self._cities = ['Paris', 'Berlin', 'Rome', 'London']
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._cities):
            raise StopIteration
        else:
            item = self._cities[self._index]
            self._index += 1
            return item

c = Cities() # <__main__.Cities object at 0x001>

# object instances of the Cities class are iterators, every time that we want to run a new loop,
# we have to create a new instance of cities. that is wasteful, cause we should not have to
# re-create the _cities every time.


# separate the object that maintains the data (_cities) from the iterator object itself:
class Cities:
    def __init__(self):
        self.data = ['Paris', 'Berlin', 'Rome', 'London']
        self.i = 0
    
    def __len__(self):
        return len(self.data)


class CityIterator:
    def __init__(self, city_obj):
        self.city_obj = city_obj   # <__main__.Cities object at 0x001>.data -> [...]
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= len(self.city_obj):
            raise StopIteration
        else:
            item = self.city_obj.data[self.i] # [...]
            self.i += 1
            return item

# instance of the container object:
cities = Cities()  # <__main__.Cities object at 0x001>

# creating the iterator object with data:
city_iter = CityIterator(cities)

# exhausting that into a iteration:
for c in city_iter: print(c)
# Paris
# Berlin
# Rome
# London

# at this point, city_iter is exhausted. if we want to re-iterate over the same collection, we
# just require to "reload" the iterator:
city_iter = CityIterator(cities)

for c in city_iter: print(c)
# Paris
# Berlin
# Rome
# London


# the drawback now i that, we have to remember to create a new iterator every time.
# would be nice if we didnt have to do that manually every time, and be ble to iterate over the
# Cities object directly instead of a separated class.

# this is where the formal definition of a Python iterable comes in.

#_____________________________________________________________________________________________________
# iterables:

# the iterable protocol requires that, the object implements a single method, the __iter__ where
# it is going to return a new instance of the iterator object.

# an iterable is an object that implements:  __iter__ -> returns an iterator (new instance)

# an iterator is an object that implements:  __iter__ -> returns itself (an iterator)
#                                            __next__ -> returns the next element.

# iterable:
s = 'Fabio'
hasattr(s, '__iter__') # True
hasattr(s, '__next__') # False

# iterator:
hasattr(iter(s), '__iter__') # True
hasattr(iter(s), '__next__') # True

# it means that, iterators are themselves iterables, but they are iterables that become exhausted.
# iterables on the other hand, will never become exhausted, cause they always return a new iterator
# object that is then used to iterate.

#_____________________________________________________________________________________________________
# built-in iter function:

# Python has a built-in function 'iter()' that calls the __iter__ method (preferred).

iter([1, 2, 3])       # <list_iterator object at 0x01>
next(iter([1, 2, 3])) # 1

# we can consume iterator objects manually:

# data (container/collection):
s = "Fabio"

# creating an iterator containing the data:
iter_s = iter(s)  # <str_iterator object at 0x001>

next(iter_s)      # F
next(iter_s)      # a
next(iter_s)      # b
iter_s.__next__() # i
iter_s.__next__() # o


# first thing Python does when we try to iterate over an object is call the iter() to obtain
# an iterator object, then it starts iterating (using next, StopIteration, etc).

# if Python doesnt find __iter__ method defined in our class, it goes and look for __getitem__.

class Cities:
    def __init__(self):
        self.data = ['Paris', 'Berlin', 'Rome', 'London']
    
    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return self.CityIterator(self)

    class CityIterator:
        def __init__(self, cities):
            self.cities = cities
            self.i = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.i >= len(self.cities):
                raise StopIteration
            else:
                item = self.cities.data[self.i]
                self.i += 1
                return item

c = Cities()

# now we can iterate over that iterable as many time we want to:
for e in c: print(e)
for e in c: print(e)
for e in c: print(e)

# every time we iterate, iter gets called on Cities and __iter__ method returns a new iterator
# where Python will call next and track the StopIteration exception to stop the loop.
