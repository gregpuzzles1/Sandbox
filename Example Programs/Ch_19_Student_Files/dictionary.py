"""
File: dictionary.py
"""

class Entry(object):
    """A key/value pair."""
    
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __eq__(self, other):
        return self.key == other.key

    def __str__(self):
        return str(self.key) + ":" + str(self.value)

class ListDict(object):
    """A list-based implementation of a dictionary."""

    def __init__(self):
        self._table = []

    def __getitem__(self, key):
        """Returns the value associated with key or
        returns None if key does not exist."""
        entry = Entry(key, None)
        try: 
            index = self._table.index(entry)
            return self._table[index].value
        except:
            return None

    def pop(self, key):
        """Removes the entry associated with key and
        returns its value or returns None if key
        does not exist."""
        entry = Entry(key, None)
        try: 
            index = self._table.index(entry)
            return self._table.pop(index).value
        except:
            return None

    def __setitem__(self, key, value):
        """Inserts an entry with key/value if key
        does not exist or replaces the existing value
        with value if key exists."""
        entry = Entry(key, value)
        try: 
            index = self._table.index(entry)
            self._table[index] = entry
        except:
            self._table.append(entry)

    # The methods __len__(), __str__(), keys(), and values()
    # are exercises


from arrays import Array

class HashEntry(Entry):

    def __init__(self, key, value, next):
        Entry.__init__(self, key, value)
        self.next = next

class HashDict(object):
    """A hashing implementation of a dictionary."""

    DEFAULT_CAPACITY = 3

    def __init__(self, capacity = None):
        if capacity is None:
            self._capacity = HashDict.DEFAULT_CAPACITY
        else:
            self._capacity = capacity
        self._table = Array(self._capacity)
        self._size = 0
        self._priorEntry = None
        self._foundEntry = None
        self._index = None

    def __contains__(self, key):
        """Returns True if key is in the dictionary or
        False otherwise."""
        self._index = abs(hash(key)) % self._capacity
        self._priorEntry = None
        self._foundEntry = self._table[self._index]
        while self._foundEntry != None:
            if self._foundEntry.key == key: 
                return True
            else:
                self._priorEntry = self._foundEntry
                self._foundEntry = self._foundEntry.next
        return False

    def __getitem__(self, key):
        """Returns the value associated with key or
        returns None if key does not exist."""
        if key in self: 
            return self._foundEntry.value
        else:
            return None 

    def pop(self, key):
        """Removes the entry associated with key and
        returns its value or returns None if key
        does not exist."""
        if not key in self:
            return None
        else:
            if self._priorEntry is None:
                self._table[self._index] = self._foundEntry.next
            else:
                self._priorEntry.next = self._foundEntry.next
            self._size -= 1 
            return self._foundEntry.value

    def __setitem__(self, key, value):
        """Inserts an entry with key/value if key
        does not exist or replaces the existing value
        with value if key exists."""
        if not key in self: 
            newEntry = HashEntry(key, value,
                                 self._table[self._index])
            self._table[self._index] = newEntry
            self._size += 1
            return None
        else:
            returnValue = self._foundEntry.value
            self._foundEntry.value = value
            return returnValue

    def __len__(self):
        return self._size

    def __str__(self):
        result = "HashDict: capacity = " +  \
                 str(self._capacity) + ", load factor = " + \
                 str(len(self) / float(self._capacity)) 
        for i in xrange(self._capacity):
            rowStr = ""
            entry = self._table[i]
            while entry != None: 
                rowStr += str(entry) + " "
                entry = entry.next
            if rowStr != "":
                result += "\nRow " + str(i) + ": " + rowStr
        return result
    # The methods keys() and values() are exercises


def main():
    d = HashDict()
    d["Name"] = "Ken"
    d["Age"] = 56
    print d
    print "Expect True:", "Name" in d
    print "Expect Ken:", d["Name"]
    print "Expect None:", d["Address"]
    d["Age"] = 57
    print "Expect 57:", d["Age"]
    print "Expect Ken:", d.pop("Name")
    print "Expect None:", d.pop("Address")

if __name__ == "__main__": main()
