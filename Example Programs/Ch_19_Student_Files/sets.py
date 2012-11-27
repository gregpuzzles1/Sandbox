"""
File: sets.py
"""

class ListSet(object):
    """A list-based implementation of a set."""

    def __init__(self):
        self._items = []

    def add(self, item):
        """Adds item to the set if it is not in the set."""
        if not item in self._items:
            self._items.append(item)

    def __iter__(self):
        return iter(self._items)

    def union(self, other):
        result = ListSet()
        for item in self:
            result.add(item)
        for item in other:
            result.add(item)
        return result

    # The methods remove, __len__, __str__, intersection,
    # and difference are exercises.


from node import Node
from arrays import Array

class HashSet(object):
    """A hashing implementation of a set."""

    DEFAULT_CAPACITY = 3

    def __init__(self, capacity = None):
        if capacity is None:
            self._capacity = HashSet.DEFAULT_CAPACITY
        else:
            self._capacity = capacity
        self._table = Array(self._capacity)
        self._size = 0
        self._priorEntry = None
        self._foundEntry = None
        self._index = None

    def __contains__(self, item):
        """Returns True if item is in the set or
        False otherwise."""
        self._index = abs(hash(item)) % self._capacity
        self._priorEntry = None
        self._foundEntry = self._table[self._index]
        while self._foundEntry != None:
            if self._foundEntry.data == item: 
                return True
            else:
                self._priorEntry = self._foundEntry
                self._foundEntry = self._foundEntry.next
        return False

    def remove(self, item):
        """Removes the item or returns None if item
        does not exist."""
        # Exercise
        
    def add(self, item):
        """Adds item to the set if it is not in the set."""
        if not item in self: 
            newEntry = Node(item,
                            self._table[self._index])
            self._table[self._index] = newEntry
            self._size += 1

    def __len__(self):
        return self._size
    
    def __iter__(self):
        # Exercise

    def __str__(self):
        # Exercise

    # The methods union, intersection, and difference are exercises

from bst import BST

class TreeSet(object):
    """A tree-based implementation of a sorted set."""

    def __init__(self):
        self._items = BST()

    def __contains__(self, item):
        """Returns True if item is in the set or
        False otherwise."""
        return self._items.find(item) != None

    def add(self, item):
        """Adds item to the set if it is not in the set.""" 
        if not item in self:
            self._items.add(item)

    # The methods remove, __len__, __str__, intersection, union,
    # and difference are exercises.


def main():
    s1 = HashSet()
    s2 = HashSet()
    s1.add("red")
    s1.add("blue")
    s2.add("green")
    s2.add("red")
    i = s1.intersection(s2)
    u = s1.union(s2)
    d = s1.difference(s2)
    for item in i: print item,
    print
    for item in u: print item,
    print
    for item in d: print item,

if __name__ == "__main__": main()

        
