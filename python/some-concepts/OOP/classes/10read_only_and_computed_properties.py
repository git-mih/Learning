# Read-only and computed properties

# to create a read-only property, we just need to create a property with only the
# get accessor defined. it is not truly read-only since underlying storage variable
# could be accessed direcly, like: obj._variable = new_value

# useful for computed properties:
import math
import re
class Circle:
	def __init__(self, r):
		self.r = r

	@property
	def area(self):
		return math.pi * (self.r ** 2)

c = Circle(1)
c.area        # 3.14...
# this way feels more natural. since area is really a property of a circle.

c.area        # calculating area...  3.14...
c.area        # calculating area...  3.14...
c.area        # calculating area...  3.14... (re-calculate again and again)



# Caching computed properties

# using property setters is sometimes useful for controlling how other computed 
# properties are cached.

# area is a computed property with lazy computation, it only calculates area 
# when requested. 
# the problem is, everytime we ask c.area it will re-calculate again and again.

# would be nice to cache the area value, so if we request the c.area and it didnt
# had changed, we just get the same value and save computation time.

# but what if someone changes the radius? we need to invalidate the cache, reseting
# whenever the radius change.
import math
class Circle:
	def __init__(self, r):
		self._r = r
		self._area = None

	@property
	def radius(self):
		return self._r

	@radius.setter
	def radius(self, r):
		if r < 0:
			raise ValueError('radius must be non-negative')
		self._r = r
		self._area = None  # invalidating cache, reseting it.

	@property
	def area(self):
# if area was changed, store new value into _area. otherwise, just return _area.
		if self._area is None:  
			print('calculating area...')
			self._area = math.pi * (self.radius ** 2) # storing the area in cache
		return self._area

c = Circle(1)

c.area        # calculating area...  3.14...
c.area        # 3.14...
c.area        # 3.14...   doesnt have to calculated if radius wasnt changed

c.radius = 2
c.__dict__    # {'_radius': 2, '_area': None}

c.area        # calculating area...  12.56...
c.area        # 12.56...


#___________________________________________________________________________________________
from urllib import request
from time import perf_counter

class WebPage:
	def __init__(self, url):   # page.url = google.com // python.org // yahoo.com
		self.url = url
		self._page = None
		self._page_size = None
		self._time = None

	@property
	def url(self):
		return self._url

	@url.setter
	def url(self, value):
		self._url = value
		self._page = None

	@property
	def page(self):
		if self._page is None: # checking in cache
			self.downlaod_page()
		return self._page
	
	@property
	def page_size(self):
		if self._page is None:
			self.download_page()
		return self._page_size
		
	@property
	def time_elapsed(self):
		if self._page is None:
			self.download_page()
		return self._time

	def download_page(self):
		self._page_size = None
		self._time = None

		start_time = perf_counter()

		with request.urlopen(self.url) as f:
			self._page = f.read()

		end_time = perf_counter()

		self._page_size = len(self._page)
		self._time = end_time - start_time

urls = [
	'https://www.google.com',
	'https://www.python.org',
	'https://www.yahoo.com'
]

for url in urls:
	page = WebPage(url) #    WebPage.page_size(page)        WebPage.time_elapsed(page)
	print(f'{url}\t size={format(page.page_size, "_")}\t elapsed={page.time_elapsed:.2f} secs')

# https://www.google.com  size=13_503     elapsed=0.24 secs
# https://www.python.org  size=50_076     elapsed=0.15 secs
# https://www.yahoo.com   size=522_263    elapsed=8.39 secs

