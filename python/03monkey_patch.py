from fractions import Fraction

def dec_speak(cls): # Monkey patching by using function, it will acts like a decorator
    cls.speak = lambda self, msg: '{0} says: {1}.'.format(cls.__name__, msg)
    return cls

Fraction = dec_speak(Fraction) # monkey patching the Fraction class. We can dir(Fraction) // 'speak' method there
f = Fraction(6, 2)
# print(f.speak('im smarter than you'))

@dec_speak     # Person = dec_speak(Person)   acting like a decorator
class Person:
    pass

p = Person()
# print(p.speak('im a human'))
