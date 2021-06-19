# decorator just to prime these generator functions
def coroutine(fn):
	def wrapper(*args, **kwargs):
		gen = fn(*args, **kwargs)
		next(gen)
		return gen
	return wrapper

@coroutine
def printing():
	while True:
		received = yield
		print(received)

@coroutine
def echo(gen_fn):
	while True:
		received = yield
		gen_fn.send(received)

print_data = printing() # gen object printing
g1 = echo(print_data)   # send to gen obj printing
g2 = echo(g1) 
g2.send('sup')          # send to gen obj echo 

#  g2 -> g1 -> print_data ------> 'sup'
# echo  echo    printing