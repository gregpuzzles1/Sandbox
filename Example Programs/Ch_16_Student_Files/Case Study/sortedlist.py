"""
File: sortedlist.py

Sorted lists include the index-based operations [] and  
remove and the content-based operations insert and index.
Items are maintained in ascending order.
"""

from indexedlist import ArrayIndexedList

class ArraySortedList(object):
    """ Array-based implementation of a sorted list."""
    
    def __init__(self):
        self._items = ArrayIndexedList()
    
    def __len__(self):
        return len(self._items)

    def isEmpty(self):
        return self._items.isEmpty()

    def __str__(self):
        return str(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        """Preconditions left as an exercise."""
        return self._items.get(index)

    def remove(self, index):
        """Preconditions left as an exercise."""
        return self._items.remove(index)
    
    def insert(self, item):
        """Inserts item in its proper place."""
        index = 0
        while index < len(self) and \
              item > self[index]:
            index += 1
        self._items.insert(index, item)

    def index(self):
        """Returns the index of the given item or -1 if
        it is not found."""
        pass   #Exercise: uses a binary search


def main():
    # Test either implementation with same code
    a = ArraySortedList()
    print "Length:", len(a)
    print "Empty:", a.isEmpty()
    
    print "Insert 3, 5, 7, 9"
    for i in xrange(3, 10, 2):
        a.insert(i)

    print "String (first to last):", a
    
    print "Length:", len(a)
    print "Empty:", a.isEmpty()
    
    print "Iterator:",
    for item in a:
        print item,
        
    print "\nGetting all:",
    for i in xrange(len(a)):
        print a.get(i),
        
    print "\nInsert 2:",
    a.insert(2)
    print a
    
    print "Insert 4:",
    a.insert(4)
    print a
    
    print "Insert 11:",
    a.insert(11)
    print a


if __name__ == '__main__': 
    main()
