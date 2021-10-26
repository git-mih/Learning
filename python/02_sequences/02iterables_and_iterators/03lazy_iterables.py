# Lazy Evaluation

# There is nothing to do with iterables, it is basically a technique that is often used in class
# properties. 
# Properties of classes may not always be populated when the object is created. Instead, the 
# value of a property only becomes known when the property is requested (deferred).

class Actor:
    def __init__(self, actor_id):
        self.actor_id = actor_id
        self.bio = lookup_actor_id_in_db(actor_id)

        # we dont populate this property, cause the actor may not have movies associated with.
        self.movies = None

    # instead, we create a property object which will consutate the database whenever we request
    # for the `movies` attribute (property).
    @property
    def movies(self):
        if self.movies is None:
            self.movies = lookup_movies_in_db(self.actor_id)
        return self.movies

# But that will only works in the first time that we request `movies`, it will go and lookup in
# the database, set the `self.movies` with the movies, and if we try to access that property 
# later on, it will already be populated.

class Circle:
    def __init__(self, r):
        self.radius = r
        self._area = None # going to cache the area value and invalidate it when change the radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self._area = None  # If we change the radius, we invalidate the area, so we can re-calculate
    
    @property
    def area(self):
        if self._area is None:
            print('Calculating area...')
            self._area = math.pi * (self.radius ** 2)
        return self._area

#_________________________________________________________________________________________________
# Applying lazy evaluation to iterables

# We can apply the same concept to certain iterables. We dont have to store all the value of a 
# iterable in order to delivery them. Instead, we can calculate the next item in an iterable only 
# when it is actually requested.

# Using Lazy evaluation technique in iterables means that, we can actually have infinite iterables.
# Since the items arent computed until they are requested, we can have an infinite number of items
# in the collection.

class Factorials:
    def __init__(self, length):
        self.length = length
    
    def __iter__(self):
        return self.FactIter(self.length)

    class FactIter:
        def __init__(self, length):
            self.length = length
            self.i = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.i >= self.length:
                raise StopIteration
            else:
                result = math.Factorial(self.i)
                self.i += 1
                return result

facts = Factorials(5)
list(facts) # [1, 1, 2, 6, 24]
