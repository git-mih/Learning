# Tuples as data structure

# if the tuple is immutable, it just means that, we cant change the reference, the memory
# address of individual elements inside the tuple. we cant add or remove elements from
# the tuple, cause by doing that, we would essentially shift all the elements inside the tuple.

# but if the element inside the tuple is a mutable object, for exemple, an list object, we
# can certainly mutate that object. 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name}, age={self.age})'
    
t = (Person('Fabio', 26), Person('Giu', 24))
id(t[0]) # 0x0001   (Person(name=Fabio, age=26), Person(name=Giu, age=24))

# we are not going to change the memory address of the tuple element by doing it:
t[0].age = 48

id(t[0]) # 0x0001   (Person(name=Fabio, age=48), Person(name=Giu, age=24))

#_______________________________________________________________________________________________
# the point of using tuples as data structure is that, we can specify meaning to positions.
# for exemple, we can specify that, the 1st element inside an tuple should be the city name,
# the 2nd should be the country and the 3rd one should mean the total population:
t = ('London', 'UK', 8_780_000)

# since tuples are sequences just like strings and lists, we can retrieve elements based on
# its index:
city = t[0]       # London
country = t[1]    # UK
population = t[2] # 8_780_000

# we can think of tuples as data records where the position of the data has meaning.
# because tuples, strings and integers are immutable objects, we are guaranteed that, the data
# and data structure for that tuple `t` will never change.
london = ('London', 'UK', 8_780_000)
new_york = ('New York', 'USA', 8_500_000)
beijing = ('Beijing', 'China', 21_000_000)


# we can have a homogeneous list object of these tuples:
cities = [
    ('London', 'UK', 8_780_000),
    ('New York', 'USA', 8_500_000),
    ('Beijing', 'China', 21_000_000),
    ('Sao Paulo', 'Brazil', 11_310_000)
]

total = sum([city[2] for city in cities])  # 49_590_000


# Dummy variables:
city, _, population = london
city       # London
population # 8_780_000

# we can also use dummy variables in extended unpacking as well:
name, age, *_, city = ('Fabio', 26, 3, 4, 5, 6, 7, 'POA')
name # Fabio
age  # 26
city # POA
_    # [3, 4, 5, 6, 7]
