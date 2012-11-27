"""
File: lisplist.py

Data and operations for Lisp-like lists.
"""

# Internal representation and basic operations

from node import Node

THE_EMPTY_LIST = None

def isEmpty(lyst):
    return lyst is THE_EMPTY_LIST

def first(lyst):
    return lyst.data

def rest(lyst):
    return lyst.next

def cons(data, lyst):
    return Node(data, lyst)
    

# Recursive list processing functions

def contains(item, lyst):
    """Returns True if item is in lyst or
    False otherwise."""
    if isEmpty(lyst):
        return False
    elif item == first(lyst):
        return True
    else:
        return contains(item, rest(lyst))

def get(index, lyst):
    """Returns the item at position index in lyst.
    Precondition: 0 <= index < length(lyst)"""
    if index == 0:
        return first(lyst)
    else:
        return get(index - 1, rest(lyst))

def length(lyst):
    """Returns the number of items in lyst."""
    if isEmpty(lyst):
        return 0
    else:
        return 1 + length(rest(lyst))

def toString(lyst):
    """Returns a string representation of lyst."""
    if isEmpty(lyst):
        return ""
    else:
        return str(first(lyst)) + " " + toString(rest(lyst))

def buildRange(lower, upper):
    """Returns a list containing the numbers from
    lower through upper."""
    if lower == upper:
        return cons(lower, THE_EMPTY_LIST)
    else:
        return cons(lower, buildRange(lower + 1, upper))

def remove(index, lyst):
    """Returns a list with the item at index removed.
    Precondition: 0 <= index < length(lyst)"""
    if index == 0:
        return rest(lyst)
    else:
        return cons(first(lyst),
                    remove(index - 1, rest(lyst)))


def main():
    lyst = THE_EMPTY_LIST
    for data in xrange(1, 6):
        lyst = cons(data, lyst)
    for index in xrange(0, 5): print get(index, lyst),
    print
    print length(lyst)
    print toString(lyst)

main()


