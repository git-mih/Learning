# Data attributes (class and instance context)

class MyClass:
	language = 'Python'

my_obj = MyClass()

# different namespaces
MyClass.__dict__ # {..., 'language': 'Python'}
my_obj.__dict__  # {}


MyClass.language # Python
# python starts looking for language attribute in MyClass namespace

my_obj.language  # Python
# python starts looking in my_obj namespace, if finds it, returns it. 
# if doesnt find, it looks up in the chain, looks in the class of my_obj (MyClass)

#_________________________________________________________________________________
MyClass.language # Python
MyClass.__dict__ # {'language': 'Python', ...}  class attributes

my_obj.__dict__  # {}

my_obj.language = 'Perl'
my_obj.__dict__  # {'language': 'Perl'} instance attributes

my_obj.language  # Perl
# Python will start looking in the instance object namespace, will find the 
# 'language' attribute and returns it. 

MyClass.language # Python
# the 'language' attribute in MyClass namespace still being 'Python'

# if we instantiate another object
other_obj = MyClass()

other_obj.__dict__   # {} 
other_obj.language   # Python 

#_________________________________________________________________________________
type(MyClass.__dict__)    # mappingproxy

type(my_obj.__dict__)     # dict
type(other_obj.__dict__)  # dict

# instance objects are regular dict type, not mappingproxy like classes

# that means, unlike classes, when we deal with an instance of a class, we can actually
# manipulate that dictionary directly, it is mutable.

class Program:
	language = 'Python'

p = Program()
p.__dict__    # {}

# we could not do it with mappingproxy objects. but with regular dict, sure.
p.__dict__['version'] = '3.7'
p.__dict__            # {'version': '3.7'}

getattr(p, 'version') # 3.7
p.version             # 3.7










