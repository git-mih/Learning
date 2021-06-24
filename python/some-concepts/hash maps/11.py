#						JSONEncoder
import json
from json import JSONEncoder 
from datetime import datetime
from pprint import pprint

# JSONEncoder default value. 
# The same that we used to use to serialize. dumps() uses it.

JSONEncoder().encode((1, 2, 3))  # '[1, 2, 3]'  <class 'str'>

json.dumps((1, 2, 3)) 			 # '[1, 2, 3]'  <class 'str'>

# JSONEncoder().encode(1+1j)
# TypeError: Object of type complex is not JSON serializable

#________________________________________________________________________________
# we can extend/modify this JSONEncoder class creating a subclass of it and
# overwriting the default method. 

# this default method is the one who gets called when objects types 
# cant be serialized by default. 
# the json.dumps(x, default=) default parameter is the responsible to call the
# JSONEncoder.default() method. we're going to overwrite this method now.

class CustomJSONEncoder(JSONEncoder):
	def default(self, arg):
		if isinstance(arg, datetime):
			return arg.isoformat()
		else:
			return super().default(arg)  # if we also cant handle a certain
#										   data type, we can pass it to the
#  										   parent class handle the error.
# We try to handle what we can and anything else we just delegate back to the
# parent class.

CustomJSONEncoder().encode((1, 2, 3))    # [1, 2, 3] <class 'str'>
custom_encoder = CustomJSONEncoder() 
custom_encoder.encode(True)              # true      <class 'str'>

custom_encoder.encode(datetime.utcnow()) # "2021-06-24T21:10:21.863184"

# custom_encoder.encode({1, 2})
# TypeError: Object of type set is not JSON serializable

# Serializing objects using our custom encoder with dumps()
json.dumps({'name': 'fabio', 'time': datetime.utcnow()},
			 cls=CustomJSONEncoder)  # we no longer pass the (default= )
# we need to pass our custom encoder class. it will create an instance
# and then call our custom default method when JSONEncoder cant serialize
# some object.
#              '{"name": "fabio", "time": "2021-06-24T21:17:45.357134"}'
# if JSONEncoder knows how to serialize, like, strings, integers, lists etc.
# then it will not run our custom encoder default method. So, we cant use
# the default method to overwrite these basic data types. str, int and so on.

#________________________________________________________________________________
# the biggest advantage of creating a subclass of JSONEncoder is that, we
# can encapsulate everything that we're going to need in there. we will just be
# required to remember to add the (cls = CustomEncoder) to be called when something
# cant be serialized by default.

# some default json.dumps parameters values
d = {
	'a': float('inf'),
	'b': float('nan')
}
# json.dumps(d, allow_nan=False)  #  by default it is allowed.

# ValueError: Out of range float values are not JSON compliant


# in python we can use any hashable element to be a dict key value.
# but JSON keys must be str, int, float, bool or None. they all is going
# to be converted to string btw.

d = {10: 'int', 10.5: 'float', 1+1j: 'complex'}
json.dumps(d, skipkeys=True) # {"10": "int", "10.5": "float"} skip invalid keys.


# default separators are (', ', ': '). we can modify it.
d = {
	'name': 'Python',
	'age': 27,
	'created_by': 'Guido van Rossum',
	'list': [1, 2, 3]
}
json.dumps(d, indent='---', separators=('>> ', '@ '))
# {
# ---"name"@ "Python">>
# ---"age"@ 27>>
# ---"created_by"@ "Guido van Rossum">>
# ---"list"@ [1, 2, 3]
# }



#________________________________________________________________________________
# here is the point. We require to pass these arguments everytime 
# we call dumps(). if we want to be consistent, we can pass these defaults to the
# subclass once.

# overwriting the __init__ default values of JSONEncoder
class CustomEncoder(JSONEncoder):        # we need to receive these *args, **kwargs
	def __init__(self, *args, **kwargs): # they are default values, such as 
		super().__init__(                # skipkeys=False, allow_nan=True and etc.
			skipkeys=True,
			allow_nan=False,
			indent='***',
			separators=('...', '##')
		)
		
	def default(self, arg):
		if isinstance(arg, datetime):
			return arg.isoformat()
		else:
			return super().default(arg)

d = {
	'time': datetime.utcnow(),
	1+1j: 'complex',
	'name': 'python'
}
json.dumps(d, cls=CustomEncoder)
# {
# ***"time"##"2021-06-24T22:32:59.004353"...
# ***"name"##"python"
# }


#________________________________________________________________________________
# customizing our serialization the way we wants to
class CustomEncoder(JSONEncoder):
	def default(self, arg):
		if isinstance(arg, datetime):
			obj = {
				'datetime': 'datetime',
				'iso': arg.isoformat(),
				'date': arg.date().isoformat(),
				'time': arg.time().isoformat(),
				'year': arg.year,
				'month': arg.month,
				'day': arg.day,
				'hour': arg.hour,
				'minute': arg.minute,
				'second': arg.second
			}
			return obj
		else:
			return super().default(arg)

log  = {'time': datetime.utcnow()}
# {'time': datetime.datetime(2021, 6, 24, 22, 44, 43, 969693)}

json.dumps(log, cls=CustomEncoder)
# {
#   "time": {
#     "datetime": "datetime",
#     "iso": "2021-06-24T22:46:19.802009",
#     "date": "2021-06-24",
#     "time": "22:46:19.802009",
#     "year": 2021,
#     "month": 6,
#     "day": 24,
#     "hour": 22,
#     "minute": 46,
#     "second": 19
#   }
# }

