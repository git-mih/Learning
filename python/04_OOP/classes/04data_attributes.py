# Attribute look up resolution and instance attributes (instance and class level):

class MyClass:
	language = 'Python'

o = MyClass() # <__main__.MyClass object at 0x001>

# as we saw, class and instace doesnt share namespaces:
MyClass.__dict__ # {..., 'language': 'Python'}
o.__dict__       # {}


# attribute look up resolution:
# to access the class attribute directly, python starts looking for tha attribute directly
# inside the class object namespace:
MyClass.language  # Python

# but object instances of that class inherits its attributes as well.
# if we try to access and instance attribute and Python doesnt find it, it looks for that
# attribute inside the enclosing scope (class namespace):
o.language  # Python

# if the object have that attribute inside its scope, it just returns:
o.language = 'Perl'
o.__dict__  # {'language': 'Perl'}
o.language  # Perl


# each object instance get its own namespace:
other_o = MyClass() # <__main__.MyClass object at 0x002>
other_o.__dict__    # {} 

other_o.language    # Python 

other_o.language = 'Java'
other_o.language    # Java

#__________________________________________________________________________________________________
# as we saw, class objects namespaces are stored inside a mappingproxy object:
type(MyClass.__dict__)  # <class 'mappingproxy'>

# but object instances doesnt store its attributes inside a mappingproxy object, they use a
# regular dictionary to store its attributes:
type(o.__dict__)        # <class 'dict'>


# it meanst that, we can actually manipulate that dictionary directly in the namespace:
class Program:
	language = 'Python'

p = Program() # <__main__.Program object at 0x0001>
p.__dict__    # {}

p.__dict__['version'] = '3.7'
p.__dict__['say_hello'] = lambda: 'hey'
p.__dict__    # {'version': '3.7', 'say_hello': <function <lambda> at 0x1234>}

p.version     # 3.7 
p.say_hello() # hey
