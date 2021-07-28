# The __set_name__ method

# lets go back to where we can use the object instances namespace to store the data. 
# instead of doing everything that we just did by storing data inside the descriptor 
# instance namespace.

# is a very handy method that gets called (once) when the descriptor is instantiated.
# x = IntegerValue() if the __set_name__ is defined in the IntegerValue class it will get
# called and the 'x' will get passed in to the __set_name__. 
# and that opens up new possibilities:
# better for error messages:
# include name of attribute that raised the exception

# useful application in descriptors used for validation


# a pretty typical application of using custom descriptors: (re-usability)
# suppose we have some attributes in a class that need to be validated each time they are set.
# we can get the property name from __set_name__, then when the __set__ gets called, we can
# do our data validation and if its OK, we gonna actually store that in the object instance
# namespace, under the same name!



