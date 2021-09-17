# iter function:

# when we call iter() on some object, it will first look if that object contains the __iter__
# method, if it doesnt, it goes and looks for the __getitem__. if the __getitem__ method is 
# defined, Python will creates a new iterator object from that.

class Squares:
    def __init__(self, n):
        self._n = n

    def __len__(self):
        return self._n

    def __getitem__(self, idx):
        if idx >= self._n:
            raise IndexError
        else:
            return idx ** 2

sq = Squares(5)         # <__main__.Squares object at 0x001>
hasattr(sq, '__iter__') # False

# creating a iterator from that sequence type object:
iter_obj = iter(sq)     # <iterator object at 0x003>

hasattr(iter_obj, '__iter__') # True
hasattr(iter_obj, '__next__') # True

# we are able to iterate over that sequence type using lazy evaluation now:
next(iter_obj) # 0
next(iter_obj) # 1
next(iter_obj) # 4
next(iter_obj) # 9
next(iter_obj) # 16
next(iter_obj) # StopIteration

# it only works if the object instance class implements the __getitem__ method at least.