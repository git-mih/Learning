# __format__ method

# is just yet another representation... We know we can use the format() function
# to precisely format certain types like: floats, dates, etc.
format(0.1, '.2f')    # 0.10
format(0.1, '.25f')   # 0.1000000000000000055511151

from datetime import datetime
datetime.utcnow()                                 # 2021-07-14 23:32:07.957151
format(datetime.utcnow(), '%a %Y-%m-%d %I:%M %p') # Wed 2021-07-14 11:32 PM


# we can also support it in our custom classes by implementing the __format__ method.
# we call the Python builtin function: format(value, format_spec) passing the
# value and the format specification that we want.

# if format_spec isnt supplied, it defaults to an empty string. and in this case, 
# Python will then use:                str(value)
# which in turn may fall back to the:  repr(value) if the __str__ isnt defined.

# implementating our own format specification is difficult.
# so we frequently delegates formatting back to another type that already supports it. 
class Person:
	def __init__(self, name, dob):
		self.name = name
		self.dob = dob

	def __format__(self, date_format_spec):
		# delegating back to the default: format(value, format_specification)
		# passing an object that does implement an formatting. (datetime object)
		dob = format(self.dob, date_format_spec)
		return f"Person('{self.name}', '{dob}')"

from datetime import datetime, date

p = Person('Fabio', date(1995, 4, 20))

# without passing the format_specification argument:
format(p)   # Person('Fabio', '1995-04-20')

# passing the format_specification argument:
format(p,'%a %Y-%m-%d %I:%M %p')
            # Person('Fabio', 'Thu 1995-04-20 12:00 AM')