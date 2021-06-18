import string

#_________________________________________________________________ Simple template
values = {'var': 'foo'}

s = string.Template('''
variable : $var
escape: $$
variable in text: ${var}iable
missing variable: $missing
''')

# by using safe, if the var isnt avaiable, it wont raise exception.
print('TEMPLATE: ', s.safe_substitute(values))

#_________________________________________________________________ Advanced template
class My_Temp(string.Template):
	delimiter = '%' # % instead of $
	idpattern = '[a-z]+_[a-z]+' # re to only allow 'a-z_a-z' words

text = '''
delimiter : %%
replaced  : %with_underscore
ignored   : %notunderscored
'''

d = {
	'with_underscore': 'replaced',   # this one will be replaced, follows the pattern we defined
	'notunderscored': 'not replaced' # dont follow the pattern
}

t = My_Temp(text)
print('modified ID pattern:')
print(t.safe_substitute(d))