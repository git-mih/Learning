# Delegating iterators

from collections import namedtuple

Person = namedtuple('Person', 'first last')

class PersonNames:
    def __init__(self, persons):
        try:
            self._persons = [f'{person.first} {person.last}' for person in persons]
        except (TypeError, AttributeError):
            self._persons = []

persons = [Person('Michael', 'Palin'), Person('Eric', 'Idle'), Person('John', 'Cleese')]
person_names = PersonNames(persons)

person_names._persons # ['Michael Palin', 'Eric Idle', 'John Cleese']


# The thing is that, we cant iterate without wknowing about `_persons`. 
for person in person_names._persons: print(person)
# Michael Palin
# Eric Idle
# John Cleese

#__________________________________________________________________________________________________________

# implementing the iterable protocol
class PersonNames:
    def __init__(self, persons):
        try:
            self._persons = [f'{person.first} {person.last}' for person in persons]
        except (TypeError, AttributeError):
            self._persons = []
        
    def __iter__(self):
        return iter(self._persons) # Delegating to the iter() function does that with the builtin list.

person_names = PersonNames(persons)

for name in person_names: print(name)
# Michael Palin
# Eric Idle
# John Cleese
