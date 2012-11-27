"""
File: indexedlist.py

Indexed lists include the index-based operations, append, 
and index. 
"""

from arrays import Array

class ArrayIndexedList(object):
    """Array implementation of an indexed list."""

    DEFAULT_SIZE = 10

    def __init__(self):
        self._items = Array(ArrayIndexedList.DEFAULT_SIZE)
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return len(self) == 0

    def __str__(self):
        result = ""
        for item in self:
            result += str(item) + " "
        return result

    def append(self, item):
        """Inserts item after the tail of the list."""
        self._items[self._size] = item
        self._size += 1

    def __getitem__(self, index):
        """Preconditions left as an exercise."""
        return self._items[index]

    def __setitem__(self, index, item):
        """Preconditions left as an exercise."""
        self._items[index] = item
    
    def insert(self, index, item):
        """Puts item at index, shifting items to the right if
        necessary."""
        #Resizing array left as an exercise.
        # Open a hole for the new item by shifting items to
        # the right by one position
        for probe in xrange(len(self), index, -1):
            self._items[probe] = self._items[probe - 1]
        self._items[index] = item
        self._size += 1

    def remove(self, index):
        """Deletes and returns item at index, shifting items 
        to the left if necessary."""
        # Preconditions left as an exercise
        oldItem = self.get(index)
        for probe in xrange(index, len(self) - 1):
            self._items[probe] = self._items[probe + 1]
        self._size -= 1
        # Resizing array left as an exercise
        return oldItem

    def index(self, item):
        """Returns the index of item if found or -1 
        otherwise."""
        pass                 # Exercise

    def __iter__(self):
        """An iterator for an array indexed list."""
        cursor = 0
        while True:
            if cursor == len(self):
                raise StopIteration
            yield self._items[cursor]
            cursor += 1
    

from node import Node

class LinkedIndexedList(object):
    """ Linked implementation of an indexed list."""

    # Instance variable head and tail reference the first
    # and the last nodes, respectively.
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return len(self) == 0

    def __str__(self):
        result = "["
        for item in self:
            result += str(item) + " "
        return result.strip() + "]"

    def append(self, item):
        """Inserts item after the tail of the list."""
        newNode = Node(item, None)
        if self.isEmpty():
            self._head = newNode
        else:
            self._tail.next = newNode
        self._tail = newNode  
        self._size += 1

    def _locate(self, index):
        """Searches for the node at position index.
        Postconditions: _currentNode refers to the ith node, if
                        there is one, or None if not.
                        _previousNode refers to the previous
                        node, if there is one, or None if not"""
        self._currentNode = self._head
        self._previousNode = None
        while index > 0:
            self._previousNode = self._currentNode
            self._currentNode = self._currentNode.next
            index -= 1

    def __setitem__(self, index, item):
        """Precondition: 0 <= index < len(list)"""
        if index < 0 or index >= len(self):
            raise Exception, "Index out of range"
        self._locate(index)
        self._currentNode.data = item
    
    def insert(self, index, item):
        """Puts item at index, shifting items to the right if
        necessary."""
        if index >= len(self):
            self.append(item)
        else:
            self._locate(index)
            newNode = Node(item, self._currentNode)
            if self._previousNode is None:
                self._head = newNode
            else:
                self._previousNode.next = newNode
            self._size += 1

    def remove(self, index):
        """Exercise."""
        pass

    def index(self, item):
        """Exercise."""
        pass

    def __iter__(self):
        """An iterator for a linked indexed list."""
        cursor = self._head
        while True:
            if cursor is None:
                raise StopIteration
            yield cursor.data
            cursor = cursor.next


def main():
    # Test either implementation with same code
    a = ArrayIndexedList()
    #a = LinkedIndexedList()
    print "Length:", len(a)
    print "Empty:", a.isEmpty()
    print "Append 1-9"
    for i in xrange(9):
        a.append(i + 1)
    print "Items (first to last):", a
    print "Iterating with a for loop:"
    for item in a: print item,
    print "\nLength:", len(a)
    print "Empty:", a.isEmpty()
    print "Insert 10 at position 2:"
    a.insert(2, 10)
    print a


if __name__ == '__main__': 
    main()
