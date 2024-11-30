""" 
Python Data Model is the tip of the iceberg of Python as a programming language which helps the developers 
write better code by using dunder(double underscore before and after of a method) methods which are also called as 
magic methods.

The Python Data Model is a description of Python as a framework. It formalizes the interfaces of the 
building blocks of the language itself, such as sequences, iterators, functions, classes, context managers, and so on.
for example: __len__ method is used to get the length of the object. __getitem__ method is used to get the item from the object.
__repr__ method is used to get the string representation of the object and used for debugging and logging (for developers)
__str__ method is used to get the informal string representation of the object used for end users.

We implement special methods when we want our objects to support and interact
with fundamental language constructs such as:
• Collections
• Attribute access
• Iteration (including asynchronous iteration using async for)
• Operator overloading
• Function and method invocation
• String representation and formatting
• Asynchronous programming using await
• Object creation and destruction
• Managed contexts using the with or async with statements
"""


import collections
from typing import Any

Card = collections.namedtuple('Card', ['rank', 'suit'])
Card.__annotations__ = {'rank': list[Any], 'suit': str}

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]