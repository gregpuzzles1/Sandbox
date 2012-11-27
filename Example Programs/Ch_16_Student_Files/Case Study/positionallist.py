"""
File: positionallist.py

Positional lists.
"""

from node import TwoWayNode

class LinkedPositionalList(object):
    """ Linked implementation of a positional list."""
    
    def __init__(self):
        self._head = TwoWayNode(None, None, None)
        self._head.next = self._head
        self._head.previous = self._head
        self._cursor = self._head
        self._lastItemPos = None
        self._size = 0

    def hasNext(self):
        return self._cursor != self._head

    def hasPrevious(self):
        return self._cursor.previous != self._head

    def first(self):
        """Moves he cursor to the first item
        if there is one."""
        if not self.isEmpty():
            self._cursor = self._head.next
            self._lastItemPos = None

    def last(self):
        """Moves the cursor to the last item
        if there is one."""
        if not self.isEmpty():
            self._cursor = self._head
            self._lastItemPos = None

    def next(self):
        """Precondition: hasNext returns True.
        Postcondition: lastItemPos refers to the node that
                       contains the data item returned."""
        if not self.hasNext():
            raise Exception, "No next item"
        self._lastItemPos = self._cursor
        self._cursor = self._cursor.next
        return self._lastItemPos.data

    def previous(self):
        """Precondition: hasPrevious returns True."""
        if not self.hasPrevious():
            raise Exception, "No previous item"
        self._lastItemPos = self._cursor.previous
        self._cursor = self._cursor.previous
        return self._lastItemPos.data

    def insert(self, item):
        """Inserts item after the current cursor position."""
        newNode = TwoWayNode(item, self._cursor.previous, self._cursor)
        self._cursor.previous.next = newNode
        self._cursor.previous = newNode
        self._size += 1
        self._lastItemPos = None

    def remove(self):
        """Removes the item most recently returned by
        next or previous.
        Precondition: insert or remove was not the most
                      recently used method."""
        if self._lastItemPos is None:
            raise Exception, "No established item to remove"
        if self._lastItemPos == self._cursor:
            self._cursor = self._cursor.next
        self._lastItemPos.previous.next = self._lastItemPos.next
        self._lastItemPos.next.previous = self._lastItemPos.previous
        self._size -= 1
        self._lastItemPos = None

    def replace(self, item):
        """Replaces the item most recently returned by
        next or previous.
        Precondition: insert or remove was not the most
                      recently used method."""
        if self._lastItemPos is None:
            raise Exception, "No established item to set"
        self._lastItemPos.data = item

    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return self._size

    def __str__(self):
        """Includes items from first through last."""
        result = ""
        probe = self._head.next
        while probe != self._head:
            result += str(probe.data) + " "
            probe = probe.next
        return result

def main():
    # Test either implementation with same code
    a = LinkedPositionalList()
    print "Length:", len(a)
    print "Empty:", a.isEmpty()
    print "Append 1-9"
    for i in xrange(9):
        a.insert(i + 1)
    print "Items (first to last):", a
    print "Forward traversal:",
    a.first()
    while a.hasNext(): print a.next(),
    print "\nBackward traversal:",
    a.last()
    while a.hasPrevious(): print a.previous(),
    print "\nInserting 10 before 3:", 
    a.first
    for count in xrange(2): a.next()
    a.insert(10)
    print a
    print "Removing 2:", 
    a.first()
    for count in xrange(2): a.next()
    a.remove()
    print a
    # Removing all
    a.first()
    while a.hasNext():
        a.next()
        a.remove()


if __name__ == '__main__': 
    main()
