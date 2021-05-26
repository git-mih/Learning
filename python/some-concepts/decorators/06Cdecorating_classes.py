# Decorating classes by monkey patching it throught function
from datetime import datetime, timezone

def info(self):     # label 'self' isnt required. we could call it anything like 'obj'. 
    result = []     # when we call:   p.debug() we are actually calling info(p)
    result.append('Time: {0}'.format(datetime.now(timezone.utc)))
    result.append('Class: {0}'.format(self.__class__.__name__))
    result.append('id: {0}'.format(hex(id(self))))

    for k, v in vars(self).items():           # vars(self) == self.__dict__ 
        result.append('{0}: {1}'.format(k, v)) # {'name':'fabio', 'last':'machado' }
    return result


def debug_info(cls):   # expecting a class object
    cls.debug = info   # cls.debug points to the info() function. 
    return cls


@debug_info    # Person = debug_info(Person)
class Person:
    def __init__(self, name, last): # expect (name, last)
        self.name = name
        self.last = last
    def get_fullname(self):
        print(self.name + self.last)


p = Person('mi', 'ich')
p.debug()      # p.debug == info(p)
# [
#   'Time: 2021-05-26 18:56:08.018039+00:00', 
#   'Class: Person', 
#   'id: 0x1f19cd02b80', 
#   'name: mi', 
#   'last: ich'
# ]
