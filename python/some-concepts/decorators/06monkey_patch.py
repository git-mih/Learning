# Monkey Patch

from fractions import Fraction
Fraction.speak = lambda self, msg: msg # Injecting a method inside Fraction class object

dir(Fraction) # we can see we have 'speak' method now

obj = Fraction(8, 5)
obj.speak('SSHEEEEEEESSHH') # no sense