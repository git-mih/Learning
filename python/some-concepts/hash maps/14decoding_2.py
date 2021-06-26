import json

from decimal import Decimal
from datetime import datetime
from fractions import Fraction

# json.loads function parameters (parse_float, int, constant)

j = '''
{
	"a": 100,
	"b": 0.2,
	"c": 0.5
}
'''
def make_decimal(arg):  # arg: '0.2' <class 'str'> // arg: '0.5' <class 'str'>
	return Decimal(arg)

# parse_float defines that, whenever the JSONDecorer see a json number to
# deserialize, it will delegate it to our custom function handle. so we can
# decide what to do with that 0.2 or 0.5 value.
json.loads(j, parse_float=make_decimal)
# {'a': 100, 'b': Decimal('0.2'), 'c': Decimal('0.5')}

# parse_int 
def make_int_binary(arg): # arg: 100  <class 'str'> 
	return bin(int(arg)) 

json.loads(j, parse_int=make_int_binary)
# {'a': '0b1100100', 'b': 0.2, 'c': 0.5}

# parse_constant
def make_const_none(arg):
	return None

j = '''
{
	"a": Infinity,
	"b": true,
	"c": null
}
'''
json.loads(j, parse_constant=make_const_none)
# {'a': None, 'b': True, 'c': None}

# we can also use them together. parse_float, parse_int and constant.

#____________________________________________________________________________
# json.loads function parameter  (object_hook x object_pairs_hook)

j = '''
{
	"a": 1,
	"b": 2,
	"c": {
		"c.1": 1,
		"c.2": 2,
		"c.3": {
			"c.3.1": 1,
			"c.3.2": 2
		}
	}
}
'''
def custom_decoder(arg):
	print('decoding: ', arg, type(arg))
	return arg

json.loads(j, object_hook=custom_decoder)
# we saw that the object_hook sends a dict for each json object it finds.
# decoding:  {'c.3.1': 1, 'c.3.2': 2}       <class 'dict'>
# decoding:  {'c.1': 1, 'c.2': 2, 'c.3': {'c.3.1': 1, 'c.3.2': 2}}    <class 'dict'>
# decoding:  {'a': 1, 'b': 2, 'c': {'c.1': 1, 'c.2': 2, 'c.3': {'c.3.1': 1, 'c.3.2': 2}}}   <class 'dict'>
# d =        {'a': 1, 'b': 2, 'c': {'c.1': 1, 'c.2': 2, 'c.3': {'c.3.1': 1, 'c.3.2': 2}}}

# the object_pair_hook sends a list of tuples containing key, value pairs
# for each json object it finds.
json.loads(j, object_pairs_hook=custom_decoder)
# decoding:  [('c.3.1', 1), ('c.3.2', 2)]   <class 'list'>
# decoding:  [('c.1', 1), ('c.2', 2), ('c.3', [('c.3.1', 1), ('c.3.2', 2)])]   <class 'list'>
# decoding:  [('a', 1), ('b', 2), ('c', [('c.1', 1), ('c.2', 2), ('c.3', [('c.3.1', 1), ('c.3.2', 2)])])]   <class 'list'>
# d =        [('a', 1), ('b', 2), ('c', [('c.1', 1), ('c.2', 2), ('c.3', [('c.3.1', 1), ('c.3.2', 2)])])]

# so we can decide how we want to work on customizing the deserialization.
