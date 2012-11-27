"""
File: stack.py
Project 16.4

Implements iterators for stacks.

Stack implementations
"""

from array import Array

class AbstractStack(object):
    """Represents the common attributes and methods of stack
    implementations."""

    def __init__(self):
        self._size = 0

    def __len__(self):
        """Returns the number of items in the stack."""
        return self._size

    def isEmpty(self):
        return len(self) == 0


class ArrayStack(AbstractStack):
    """ Array-based stack implementation."""

    DEFAULT_CAPACITY = 10  # Class variable for all array stacks
    
    def __init__(self):
        AbstractStack.__init__(self)
        self._items = Array(ArrayStack.DEFAULT_CAPACITY)
        self._top = -1

    def push(self, newItem):
        """Inserts newItem at top of stack."""
        # Resize array if necessary
        if len(self) == len(self._items):
            temp = Array(2 * len(self))
            for i in xrange(len(self)):
                temp[i] = self._items[i]
            self._items = temp
        # newItem goes at logical end of array
        self._top += 1
        self._size += 1
        self._items[self._top] = newItem

    def pop(self):
        """Removes and returns the item at top of the stack.
        Precondition: the stack is not empty."""
        if self.isEmpty():
            raise AttributeError, "Stack is empty"
        oldItem = self._items[self._top]
        self._top -= 1
        self._size -= 1
        if len(self) <= len(self._items) / 4 and \
           len(self) > ArrayStack.DEFAULT_CAPACITY:
            # Shrink the size by half but not below the default capacity
            # and remove those garbage cells from the underlying list
            newSize = max(ArrayStack.DEFAULT_CAPACITY,
                          len(self._items) / 2)
            temp = Array(newSize)          # Create new array
            for i in xrange(len(self)):    # Copy data from old array 
                temp [i] = self._items[i]  # to new array
            self._items = temp             # Reset old array variable to new array
        return oldItem

    def peek(self):
        """Returns the item at top of the stack.
        Precondition: the stack is not empty."""
        if self.isEmpty():
            raise AttributeError, "Stack is empty"
        return self._items[self._top]

    def __str__(self):
        """Items strung from bottom to top."""
        result = ""
        for i in xrange(len(self)):
            result += str(self._items[i]) + " "
        return result

    def __iter__(self):
        """An iterator for an array stack."""
        cursor = len(self) - 1
        while True:
            if cursor == -1:
                raise StopIteration
            yield self._items[cursor]
            cursor -= 1


from node import Node

class LinkedStack(AbstractStack):
    """ Link-based stack implementation."""

    def __init__(self):
        AbstractStack.__init__(self)
        self._top = None

    def push(self, newItem):
        """Inserts newItem at top of stack."""
        self._top = Node(newItem, self._top)
        self._size += 1

    def pop(self):
        """Removes and returns the item at top of the stack.
        Precondition: the stack is not empty."""
        if self.isEmpty():
            raise AttributeError, "Stack is empty"
        oldItem = self._top.data
        self._top = self._top.next
        self._size -= 1
        return oldItem

    def peek(self):
        """Returns the item at top of the stack.
        Precondition: the stack is not empty."""
        if self.isEmpty():
            raise AttributeError, "Stack is empty"
        return self._top.data

    def __str__(self):
        """Items strung from bottom to top."""
        
        # Helper recurses to end of nodes
        def strHelper(probe):
            if probe is None:
                return ""
            else:
                return strHelper(probe.next) + \
                       str(probe.data) + " "
            
        return strHelper(self._top)

    def __iter__(self):
        """An iterator for a linked stack."""
        cursor = self._top
        while True:
            if cursor is None:
                raise StopIteration
            yield cursor.data
            cursor = cursor.next



def main():
    # Test either implementation with same code
    s = ArrayStack()
    #s = LinkedStack()
    print "Length:", len(s)
    print "Empty:", s.isEmpty()
    print "Push 1-10"
    for i in xrange(10):
        s.push(i + 1)
    print "Iterator:",
    for item in s: print item,


if __name__ == '__main__': 
    main()
