"""
File: queue.py

Queue implementations
"""

from arrays import Array

class ArrayQueue(object):
    """ Array-based queue implementation."""

    DEFAULT_SIZE = 10  # Class variable applies to all queues
    
    def __init__(self):
        self._items = Array(ArrayQueue.DEFAULT_SIZE)
        self._rear = -1
        self._size = 0

    def enqueue(self, newItem):
        """Inserts newItem at top of queue."""
        # Resize array if necessary
        if len(self) == len(self._items):
            temp = Array(2 * self._size)
            for i in xrange(len(self)):
                temp[i] = self._items[i]
            self._items = temp
        # newItem goes at logical end of array
        self._rear += 1
        self._size += 1
        self._items[self._rear] = newItem

    def dequeue(self):
        """Removes and returns the item at front of the queue.
        Precondition: the queue is not empty."""
        oldItem = self._items[0]
        for i in xrange(len(self) - 1):
            self._items[i] = self._items[i + 1]
        self._rear -= 1
        self._size -= 1
        # Resizing the array is an exercise
        return oldItem

    def peek(self):
        """Returns the item at front of the queue.
        Precondition: the queue is not empty."""
        return self._items[0]

    def __len__(self):
        """Returns the number of items in the queue."""
        return self._size

    def isEmpty(self):
        return len(self) == 0

    def __str__(self):
        """Items strung from front to rear."""
        result = ""
        for i in xrange(len(self)):
            result += str(self._items[i]) + " "
        return result


from node import Node

class LinkedQueue(object):
    """ Link-based queue implementation."""

    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def enqueue(self, newItem):
        """Inserts newItem at rear of queue."""
        newNode = Node (newItem, None)
        if self.isEmpty():
            self._front = newNode
        else:
            self._rear.next = newNode
        self._rear = newNode  
        self._size += 1

    def dequeue(self):
        """Removes and returns the item at front of the queue.
        Precondition: the queue is not empty."""
        oldItem = self._front.data
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return oldItem

    def peek(self):
        """Returns the item at front of the queue.
        Precondition: the queue is not empty."""
        return self._front.data

    def __len__(self):
        """Returns the number of items in the queue."""
        return self._size

    def isEmpty(self):
        return len(self) == 0

    def __str__(self):
        """Items strung from front to rear."""
        result = ""
        probe = self._front
        while probe != None:
            result += str(probe.data) + " "
            probe = probe.next
        return result

class LinkedPriorityQueue(LinkedQueue):
    """Sorted list implementation using a linked structure."""

    def __init(self):
        LinkedQueue.__init__(self)

    def enqueue(self, newItem):
        """Inserts newItem after items of greater or equal
        priority or ahead of items of lesser priority.
        A has greater priority than B if A < B."""
        
        if self.isEmpty() or newItem >= self._rear.data:
            # New item goes at rear
            LinkedQueue.enqueue(self, newItem)
        else:
            # Search for a position where it's less
            probe = self._front
            while newItem >= probe.data:
                trailer = probe
                probe = probe.next
            newNode = Node(newItem, probe)
            if probe == self._front:
                # New item goes at front
                self._front = newNode
            else:
                # New items goes between two nodes
                trailer.next = newNode
            self._size += 1

class Comparable(object):
    """Wrapper class for items that are not comparable."""

    def __init__(self, item, priority):
        self._item = item
        self._priority = priority

    def __cmp__(self, other):
        if type(other) != type(self):
            raise TypeError, "Type must be Comparable"
        return cmp(self._priority, other._priority)

    def getItem(self):
        return self._item

    def __str__(self):
        return str(self._item)
