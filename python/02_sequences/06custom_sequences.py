# Custom sequences:

# custom mutable sequence type:

# in general, we expect that, whenever we perform a concatenation of two sequence objects, the 
# result is a new sequence object of the same type. but if we want to mutate an custom sequence 
# object, we should use in-place concatenation that will mutate the object, and not create a 
# new one.

class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'MyClass(name={self.name})'

    # concatenation:
    def __add__(self, other):
        return Person(self.name + other.name)

    # in-place concatenation:
    def __iadd__(self, other):
        if isinstance(other, Person):
            self.name += other.name
        else:
            self.name += other
        return self

    # repetition concatenation:
    def __mul__(self, n):
        return Person(self.name * n)
    
    # in-place repetition concatenation:
    def __imul__(self, n):
        self.name *= n
        return self

# concatenation (new object):
p1 = Person('Fabio')    # MyClass(name=Fabio)    <__main__.Person object at 0x01111>
p2 = p1 + Person('Giu') # MyClass(name=FabioGiu) <__main__.Person object at 0x02222>

p1 = Person('Fabio')    # MyClass(name=Fabio)      <__main__.Person object at 0x01111>
p2 = p1 * 2             # MyClass(name=FabioFabio) <__main__.Person object at 0x02222>


# in-place concatenation:
p1 = Person('Fabio')    # MyClass(name=Fabio)    <__main__.Person object at 0x01111>
p1 += Person('Giu')     # MyClass(name=FabioGiu) <__main__.Person object at 0x01111>

p1 = Person('Fabio')    # MyClass(name=Fabio)      <__main__.Person object at 0x01111>
p1 *= 2                 # MyClass(name=FabioFabio) <__main__.Person object at 0x01111>



# we saw earlier how we can access elements in a custom sequence type by using the __getitem__.
# but we can also handle assignments by implementing the __setitem__ method.







