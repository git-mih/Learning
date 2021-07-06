# Single inheritence

#         o------ Shape -------o
#      Ellipse              Polygon
#         |                 |     |
#         o                 o     o
#      Circle        Retangle     Triangle
#                       |
#                       o
#                     Square
class Shape:
	pass

class Ellipse(Shape):
	pass

class Circle(Ellipse):
	pass

class Polygon(Shape):
	pass

class Retangle(Polygon):
	pass

class Triangle(Polygon):
	pass

class Square(Retangle):
	pass

# sibling classes
issubclass(Ellipse, Polygon) # False

issubclass(Ellipse, Shape)   # True
issubclass(Circle, Ellipse)  # True

issubclass(Square, Shape)    # True, Square -> Retangle -> Polygon -> Shape
issubclass(Square, Square)   # True

# issubclass() must compare classes only. not instances
s = Shape()
c = Circle()
# issubclass(c, s)   # TypeError

#_______________________________________________________________________________
# type() and isinstance()

# type() doesnt look at inheritence, it looks at which class
# that particular object was directly instantiated from
type(Shape) # <class 'type'>
type(s)     # <class '__main__.Shape'>
# the type() is very specific to which class wass used to
# create the object.

# isinstance() doesnt care about inheritence, it looks to the 
# class chain only.
sq = Square()
isinstance(sq, Shape)    # True
isinstance(sq, Retangle) # True


# isinstance() is used mostly to know if given class 
# have properties of another class. like:
isinstance(sq, Polygon) # does the square instance have properties of a
#                         Polygon? does it have functionality of a Polygon?

#_______________________________________________________________________________
# mixing isinstance() and type()
sq = Square()
p = Polygon()

# we cant see if these instances are subclasse of some parent class like: 
# issubclass(sq, p)  TypeError

# we also cant use isinstance(), cause it requires a instance lhs and a class rhs
# isinstance(sq, p)  TypeError

# but we do can know what class 'p' or 'sq' was instantiated from by using type()
# the sq object is instance of <class '__main__.Polygon'>
isinstance(sq, type(p))       # True

# type(sq) <class '__main__.Square'> is subclass of type(p) <class '__main__.Polygon'>
issubclass(type(sq), type(p)) # True

#_______________________________________________________________________________
# python will make the Shape class inherit from 'object' class
type(object)   # <class 'type'>

# we arent explicitly inheriting from 'object'. Python does it for us.
class Person:
	pass

issubclass(Person, object) # True
issubclass(Square, object) # True
