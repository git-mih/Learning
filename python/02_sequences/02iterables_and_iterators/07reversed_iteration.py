# Reverse iteration (sequences and iterables)

# Lets see how we iterate over a sequence type in reverse order first.

# if we have a sequence type, then iterating over the sequence in reverse order is quite simple,
# we could do it in two different ways, for exemple:

# The bellow code downside is that, it makes a copy of the entire sequence 
# for i in seq[::-1]: print(i)

# # The following two does the same, is kinda messy but it is more efficient though
# for i in range(len(seq)): 
#     print(seq[len(seq) - i - 1])

# for i in range(len(seq)-1, -1, -1): 
#     print(seq[i])

# # Using the built-in reversed function and passing a sequence instead.
# for i in reversed(seq): print(i)

# This last approach is cleaner and efficient as well, because it creates an iterator that will
# iterate backwards over the sequence. It wont copy the data like the first exemple.

# But, to be able to use the reversed() function, the sequence requires to implement the __len__
# and the __getitem__ method. The __len__ is required because, to be able to iterate backwards,
# we require to know the last element index, and without the length of the senquence, we cant know.

class Squares:
    def __init__(self, length):
        self.squares = [i ** 2 for i in range(length)]

    def __len__(self):
        return len(self.squares)
    
    def __getitem__(self, i):
        return self.squares[i]

for num in Squares(4): print(num)
# 0
# 1
# 4
# 9

for num in reversed(Squares(4)): print(num)
# 9
# 4
# 1
# 0


# We can override how reversed words by implementing the __reversed__ method inside our classes,
# either for sequence types or iterables.


#____________________________________________________________________________________________________
# That was about the sequence types, lets see how iterating an iterable in reverse now.

# When we call the reversed() function on a custom iterable, Python will looks for and call the
# __reversed__ method. And we require to provide it to be able to work with custom iterables, cause
# the reversed() function only handle (by default) sequence types.

# The __reversed__ method should return an iterator object, which is going to be used to perform
# the reversed iteration.

# Just like the iter() function, when we call reversed() on an object, it will first looks for the
# __reversed__ method. If it doesnt find the __reversed__, then it wil use the __getitem__ and the
# __len__ methods to create an iterator for us. Otherwise, an exception is raised.

from collections import namedtuple

SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
RANKS = tuple(range(2, 11)) + tuple('JQKA')

Card = namedtuple('Card', 'rank suit')

class CardDeck:
    def __init__(self):
        self.length = len(SUITS) * len(RANKS) # 4 * 13 = 52
    
    def __len__(self):
        return self.length
    
    def __iter__(self):
        return self.CardDeckIterator(self.length)
    
    def __reversed__(self):
        return self.CardDeckIterator(self.length, reverse=True)
    
    class CardDeckIterator:
        def __init__(self, length, reverse=False):
            self.length = length
            self.reverse = reverse
            self.i = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.i >= self.length:
                raise StopIteration
            else:
                if self.reverse:
                    index = self.length - 1 - self.i  # 52 - 1 = idx[51 - 0] // idx[51 - 1] ...
                else:
                    index = self.i # idx[0] // idx[1] ...

                suit = SUITS[index // len(RANKS)]
                rank = RANKS[index % len(RANKS)]
                self.i += 1
                return Card(rank, suit)

deck = CardDeck()

for card in deck: print(card)
# Card(rank=2, suit='Spades')
# Card(rank=3, suit='Spades')
# Card(rank=4, suit='Spades')
# Card(rank=5, suit='Spades')
# Card(rank=6, suit='Spades')
# Card(rank=7, suit='Spades')
# Card(rank=8, suit='Spades')
# ...

# Reversing manually:
deck = list(CardDeck())
for card in deck[:-8:-1]: print(card) # 7 last cards of the deck
# Card(rank='A', suit='Clubs')
# Card(rank='K', suit='Clubs')
# Card(rank='Q', suit='Clubs')
# Card(rank='J', suit='Clubs')
# Card(rank=10, suit='Clubs')
# Card(rank=9, suit='Clubs')
# Card(rank=8, suit='Clubs')


# Reversing using the __reversed__ method:
for card in reversed(deck): print(card)
# Card(rank='A', suit='Clubs')
# Card(rank='K', suit='Clubs')
# Card(rank='Q', suit='Clubs')
# Card(rank='J', suit='Clubs')
# Card(rank=10, suit='Clubs')
# Card(rank=9, suit='Clubs')
# Card(rank=8, suit='Clubs')
# ...
