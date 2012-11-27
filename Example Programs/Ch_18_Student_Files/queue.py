"""
File: queue.py

A heap-based priority queue.
"""

from heap import ArrayHeap


class HeapPriorityQueue(ArrayHeap):
    """Heap-based implementation of a priority queue."""

    def __init__(self):
        ArrayHeap.__init__(self)

    def enqueue(self, item):
        self.add(item)

    def dequeue(self):
        return self.pop()

    def __str__(self):
        result = ""
        for item in self:
            result += str(item) + " "
        return result

    
def main():
    # Test any implementation with same code
    q = HeapPriorityQueue()
    #q = LinkedQueue()
    print "Length:", len(q)
    print "Empty:", q.isEmpty()
    print "Enqueue 1-10"
    for i in xrange(10):
        q.enqueue(i + 1)
    print "Peeking:", q.peek()
    print "Items (front to rear):",  q
    print "Length:", len(q)
    print "Empty:", q.isEmpty()
    print "Enqueue 0"
    q.enqueue(0)
    print "Dequeuing items (front to rear):",
    while not q.isEmpty(): print q.dequeue(),
    print "\nLength:", len(q)
    print "Empty:", q.isEmpty()



class AbstractQueue(object):
    """Common data and methods for queue implementations."""

    def __init__(self):
        self._size = 0

    def __len__(self):
        """Returns the number of items in the queue."""
        return self._size

    def isEmpty(self):
        return len(self) == 0
    

from node import Node

class LinkedQueue(AbstractQueue):
    """ Link-based queue implementation."""

    def __init__(self):
        AbstractQueue.__init__(self)
        self._front = None
        self._rear = None

    def enqueue(self, newItem):
        """Adds newItem to the rear of queue."""
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
        if self.isEmpty():
            raise AttributeError, "The queue is empty"
        oldItem = self._front.data
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return oldItem

    def peek(self):
        """Returns the item at front of the queue.
        Precondition: the queue is not empty."""
        if self.isEmpty():
            raise AttributeError, "The queue is empty"
        return self._front.data

    def __str__(self):
        """Items strung from front to rear."""
        result = ""
        probe = self._front
        while probe != None:
            result += str(probe.data) + " "
            probe = probe.next
        return result

from arrays import Array

class ArrayQueue(AbstractQueue):
    """ Array-based queue implementation."""

    DEFAULT_CAPACITY = 10  # Class variable applies to all queues
    
    def __init__(self):
        AbstractQueue.__init__(self)
        self._items = Array(ArrayQueue.DEFAULT_CAPACITY)
        self._rear = -1
        self._front = 0

    def enqueue(self, newItem):
        """Adds newItem to the rear of queue."""
        # Resize array if necessary
        if len(self) == len(self._items):
            temp = Array(2 * self._size)
            for i in xrange(len(self)):
                # Add 1 to front and wrap around array if necessary
                temp[i] = self._items[(self._front + i) % len(self._items)]
            self._items = temp
            self._front= 0
            self._rear = len(self) - 1
        # Add 1 to rear and wrap around array if necessary
        self._rear = (self._rear + 1) % len(self._items)
        self._size += 1
        self._items[self._rear] = newItem

    def dequeue(self):
        """Removes and returns the item at front of the queue.
        Precondition: the queue is not empty."""
        if self.isEmpty():
            raise AttributeError, "The queue is empty"
        oldItem = self._items[self._front]
        self._size -= 1
        if self.isEmpty():
            # Reset pointers to initial state
            self._rear = -1
            self._front = 0
        else:
            # Add 1 to front and wrap around array if necessary
            self._front = (self._front + 1) % len(self._items)
        # Resizing the array is an exercise
        if len(self) <= len(self._items) / 4 and \
           len(self) > ArrayQueue.DEFAULT_CAPACITY:
            # Shrink the size by half but not below the default capacity
            # and remove those garbage cells from the underlying list
            newSize = max(ArrayQueue.DEFAULT_CAPACITY,
                          len(self._items) / 2)
            temp = Array(newSize)          # Create new array
            for i in xrange(len(self)):
                temp[i] = self._items[(self._front + i) % len(self._items)]
            self._items = temp
            self._front= 0
            self._rear = len(self) - 1
        return oldItem

    def peek(self):
        """Returns the item at front of the queue.
        Precondition: the queue is not empty."""
        if self.isEmpty():
            raise AttributeError, "The queue is empty"
        return self._items[self._front]

    def __str__(self):
        """Items strung from front to rear."""
        result = ""
        for i in xrange(len(self)):
            result += str(self._items[(self._front + i) % len(self._items)]) + " "
        return result


if __name__ == '__main__': 
    main()
