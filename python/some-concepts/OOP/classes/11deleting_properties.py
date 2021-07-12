# Deleting properties

class MyClass:
	pass

# just like we can delete attributes from an object instance:
obj = MyClass()
obj.name = 'fabio'
del obj.name
# obj.name  AttributeError

# we can also delete properties from an object instance by using the fdel argument 
# of the property initializer or the deleter method of property object.

# but now when we talk about the del keyword, we are actually doing it at the
# object instance namespace. 
# it happens because we are calling a method that is bound to an object instance.

# calling the deleter runs code contained in the deleter method, is all it does,
# doesnt remove the property from class itself.
class Color:
	def __init__(self, color):
		self._color = color

	def get_color(self):
		return self._color

	def set_color(self, value):
		self._color = value

    # when this method is invoked, it will remove _color from the object instance namespace
	def del_color(self):
		del self._color

	color = property(get_color, set_color, del_color)

c = Color('red')   # c.__dict__   {'_color': 'red'}

c.color    # red
del c.color        # c.__dict__   {}