#						CUSTOM JSON ENCODING
import json

from pprint import pprint
from datetime import datetime
from decimal import Decimal


datetime.utcnow() # datetime.datetime(2021, 6, 24, 15, 16, 43, 844604)
# json.dumps(datetime.utcnow())
# TypeError: Object of type datetime is not JSON serializable

# converting date object to string type 
datetime.utcnow().isoformat() # 2021-06-24T15:21:32.589284 <class 'str'>

# or we can format it ourselfs
def format_iso(dt):
	return dt.strftime('%Y-%m-%dT%H:%M:%S')

format_iso(datetime.utcnow()) # 2021-06-24T15:20:35        <class 'str'>

# we are now able to serialize it by passing strings instead 
# datetime objects that JSONEncoder cant handle
log = {'time': datetime.utcnow().isoformat(), 'message': 'testing...'}
json.dumps(log)
# {
#   "time": "2021-06-24T15:25:54.991425", 
#   "message": "testing..."
# }

log = {'time': format_iso(datetime.utcnow())}
json.dumps(log)
# {
#   "time": "2021-06-24T15:25:54",
#   "message": "testing..."
# }

#____________________________________________________________________________
# json.dumps default parameter             (default = our_handler_fn)

# whenever JSONEncoder encounters a object that it doesnt know how to
# serialize, it is going to call our function instead and ask us how
# we want it to be serialized. 

# our logs should have the datetime and any object inserted directly
log = {'time': datetime.utcnow()}
# log = {'time': datetime.datetime(2021, 6, 24, 17, 59, 48, 555685)}

json.dumps(log, default=format_iso) 
# {
#   "time": "2021-06-24T15:44:38",
#   "message": "testing..."
# }

# elements that JSONEncoder cant serialize,
# will be passed as argument to our handler. one by one,
def handler(data): # data = 2021-06-24T15:44:38   //  data = {1, 2}
	return 'handler function trying to serialize...'

log = {'time': datetime.utcnow(), 'message': 'testing', 'set': {1, 2}}
json.dumps(log, indent=2, default=handler)
# {
#   "time": "handler function trying to serialize...",
#   "message": "testing",
#   "set": "handler function trying to serialize..."
# }

# that function get called whenever JSONEncoder cant serialize a object

#____________________________________________________________________________
# tweaking our handler to be able to handle different data types
def handler(arg):
	if isinstance(arg, datetime): 
		return arg.isoformat()
	elif isinstance(arg, set):
		return list(arg)

log = {'time': datetime.utcnow(), 'message': 'testing', 'set': {1, 2}}
json.dumps(log, default=handler)
# {
#   "time": "2021-06-24T16:39:30.005326",  -> datetime.isoformat()
#   "message": "testing",
#   "set": [1, 2]                          -> list( {1, 2} )
# }

# creating a custom object
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.create_dt = datetime.utcnow()

	def toJSON(self):
		return {
			'name': self.name,
			'age': self.age,
			'create_dt': self.create_dt.isoformat()
		}

p = Person('fabio', 26)
p.toJSON() 
# {'name': 'fabio', 'age': 26, 'create_dt': '2021-06-24T16:48:34.519576'}

log = dict(time= datetime.utcnow(),
		   message='Created new person record.',
		   person = p  # not using toJSON() but we could.
		   )

json.dumps(log, default=handler) # it can handle, but..
# {
#   "time": "2021-06-24T16:51:48.975901",
#   "message": "Created new person record.",
#   "person": null
# }
# our handler returns None, we did not provided a custom serialization to Person obj.

#____________________________________________________________________________
# extending the handler to serialize our custom Person object
def handler(arg):
	if isinstance(arg, datetime):  # datetime handler
		return arg.isoformat()
	elif isinstance(arg, set):     # set handler
		return list(arg)
	elif isinstance(arg, Person):  # Person obj handler
		return arg.toJSON()

json.dumps(log, default=handler)
# {
#   "time": "2021-06-24T17:01:57.207702",
#   "message": "Created new person record.",
#   "person": {
#     "name": "fabio",                 #  worked properly now.
#     "age": 26,
#     "create_dt": "2021-06-24T17:01:57.207702"
#   }
# }


# we can let the JSONEncoder reach the "create_dt" key and then delegate to our 
# handler function serialize it.
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.create_dt = datetime.utcnow()

	def toJSON(self):
		return vars(self) # no longer need isoformat()

p = Person('fabio', 26)

json.dumps({'person': p}, default=handler)
# {
#   "person": {
#     "name": "fabio",
#     "age": 26,
#     "create_dt": "2021-06-24T17:08:23.244517"
#   }
# }

#____________________________________________________________________________
class Point:
	def __init__(self, x, y): # we can make a vars(self) making a dict using
		self.x = x            # Point attributes x, y. 
		self.y = y            # eg:   {'x': 4, 'y': 7}

# making our handler more generic
def handler(arg):
	if isinstance(arg, datetime):
		return arg.isoformat()
	elif isinstance(arg, set):
		return list(arg)
	else:
		try:
			return arg.toJSON()
		except AttributeError:   # AttributeError: 'Point' has no attribute 'toJSON'.
			try:
				return vars(arg) # trying to return a dict w/all attributes of arg obj
			except TypeError:    # if it fails, the arg obj doesnt have any attribute.
				return str(arg)  # we return string of arg, whatever it might be...

log = dict(person= Person('fabio', 26),
		   point = Point(4, 7),
		   number= 1+1j,
		   set_ = {1, 2, 3})

json.dumps(log, indent=2, default=handler)
# {
#   "person": {          -> arg.toJSON()
#     "name": "fabio",
#     "age": 26,
#     "create_dt": "2021-06-24T17:35:48.288392"  -> arg.isoformat()
#   },
#   "point": {           -> vars(arg)
#     "x": 4,
#     "y": 7
#   },
#   "number": "(1+1j)",  -> str(arg)
#   "set_": [1, 2, 3]    -> list(arg)
# }

#____________________________________________________________________________
# another exemple
pt1 = Point(1, 2)
pt2 = Point(Decimal(5.87), Decimal(9.2))
p = Person('fabio', 26)

log = dict(
	time=datetime.utcnow(),
	message='created new points',
	point1=pt1,
	point2=pt2,
	created_by=p
)
# log = 
# {'created_by': <__main__.Person object at 0x000002707C642730>,
#  'message': 'created new points',
#  'point1': <__main__.Point object at 0x000002707C35A7C0>,
#  'point2': <__main__.Point object at 0x000002707C642790>,
#  'time': datetime.datetime(2021, 6, 24, 17, 52, 55, 774497)}

json.dumps(log, default=handler)
# {
#   "time": "2021-06-24T17:48:35.500266",
#   "message": "created new points",
#   "point1": {
#     "x": 1,
#     "y": 2
#   },
#   "point2": {
#     "x": "5.8700000",   -> str(arg)
#     "y": "9.1999999",   -> str(arg)
#   },
#   "created_by": {
#     "name": "fabio",
#     "age": 26,
#     "create_dt": "2021-06-24T17:48:35.500266"
#   }
# }

#____________________________________________________________________________
#						USING SINGLE DISPATCH

from functools import singledispatch

@singledispatch
def handler(arg):
	try:
		return arg.toJSON()
	except AttributeError:
		try:
			return vars(arg)
		except TypeError:
			return str(arg)

@handler.register(datetime)   # if isinstance(arg, datetime) ...
def _(arg):
	return arg.isoformat()

@handler.register(set)        # if isinstance(arg, set) ...
def _(arg):
	return list(arg)

# we could also had registered Point and Person. But we are handling
# with them inside the handler 

# @handler.register(Person)
# def _(arg):
# 	return arg.toJSON()

# @handler.register(Point)
# def _(arg):
# 	return vars(arg)

log = {
	'time': datetime.utcnow(),
	'message': 'Created new point',
	'point': pt1,
	'created_by': p
}

json.dumps(log, default=handler)
# {
#   "time": "2021-06-24T19:19:14.156344",
#   "message": "Created new point",
#   "point": {
#     "x": 1,
#     "y": 2
#   },
#   "created_by": {
#     "name": "fabio",
#     "age": 26,
#     "create_dt": "2021-06-24T19:19:14.152389"
#   }
# }