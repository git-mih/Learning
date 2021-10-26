# iter function

# What happens when Python performs an iteration over a iterable object? For exemple, when Python 
# encounter a loop (for, while, list comprehension, etc), it will call the `iter()` function.

# The iter() function expect any kind of iterable object, and returns an iterator from that.

# when we call iter() on some object, it will first look if that object contains the __iter__
# method, if it doesnt, it goes and looks for the __getitem__. 

# if only the __getitem__ method is defined, Python will creates a new iterator object from that 
# and will iterate over it. But if we dont implement either the __iter__ nor __getitem__, the
# object isnt iterable at all, and Python will raise an Exception for that.


# If we want, we can implement the __iter__ inside our custom classes, and be able to call the
# iter() function which is going to return a iterator object, with that, we can iterate over that
# new iterator.


# Python does that essentially, whenever we went to a loop, it calls the iter() function (
# not necessarally the __iter__ method), and iterate over the iterator. Therefore, if the object
# doesnt have the __iter__ method, it doesnt matter, as long the object support the __getitem__
# method, it will go and make a iterator with that. In practice, the iter() function will first
# try to use __iter__, if it doesnt find, it looks for the __getitem__ method and use that in
# order to create the iterator and iterate over it.

# Making an iterator to iterate over any Sequence type:
class Squares:
    def __init__(self, n):
        self._n = n

    def __len__(self):
        return self._n

# We are not implementing the __iter__ method, but we are going to get an iterator from it as well.
    def __getitem__(self, i):
        if i >= self._n:
            raise IndexError
        else:
            return i ** 2

sq = Squares(5)
hasattr(sq, '__iter__') # False

# We can use the iter() function to get an iterator from that sequence object
sq_iter = iter(sq) # iterator

next(sq_iter) # 0
next(sq_iter) # 1
next(sq_iter) # 4
for i in sq_iter: print(i)
# 9
# 16
    
# Manually representing what the iter() function is doing, basically
class SequenceIterator:
    def __init__(self, sequence): # expecting a iterable object
        self.sequence = sequence
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= len(self.sequence):
            raise StopIteration
        else:
            result = self.sequence[self.i]
            self.i += 1
            return result

sq = Squares(5)
sq_iterator = SequenceIterator(sq)
next(sq_iterator) # 0
next(sq_iterator) # 1 
next(sq_iterator) # 4
for i in sq_iterator: print(i)
# 9
# 16

# To check whether an object is iterable or not, we could just call the iter() function, it will
# check if the object have (__iter__ + __next__), or if it have (__getitem__) method. otherwise,
# it throws an exception.
