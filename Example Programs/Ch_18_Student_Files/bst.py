"""
File: bst.py
BST class for binary search trees.
"""

from queue import LinkedQueue
from binarytree import BinaryTree

class BST(object):

    def __init__(self):
        self._tree = BinaryTree.THE_EMPTY_TREE
        self._size = 0


    def isEmpty(self):
        return len(self) == 0

    def __len__(self):
        return self._size

    def __str__(self):
        return str(self._tree)

    def __iter__(self):
        return iter(self.inorder())

    def find(self, target):
        """Returns data if target is found or None otherwise."""
        def findHelper(tree):
            if tree.isEmpty():
                return None
            elif target == tree.getRoot():
                return tree.getRoot()
            elif target < tree.getRoot():
                return findHelper(tree.getLeft())
            else:
                return findHelper(tree.getRight())
            
        return findHelper(self._tree)

    def add(self, newItem):
        """Adds newItem to the tree."""

        # Helper function to search for item's position 
        def addHelper(tree):
            currentItem = tree.getRoot()
            left = tree.getLeft()
            right = tree.getRight()

            # New item is less, go left until spot is found
            if newItem < currentItem:
                if left.isEmpty():
                    tree.setLeft(BinaryTree(newItem))
                else:
                    addHelper(left)                    

            # New item is greater or equal, 
            # go right until spot is found
            elif right.isEmpty():
                tree.setRight(BinaryTree(newItem))
            else:
                addHelper(right)
            # End of addHelper

        # Tree is empty, so new item goes at the root
        if self.isEmpty():
            self._tree = BinaryTree(newItem)

        # Otherwise, search for the item's spot
        else:
            addHelper(self._tree)
        self._size += 1

    def inorder(self):
        """Returns a list containing the results of
        an inorder traversal."""
        lyst = []
        self._tree.inorder(lyst)
        return lyst


    def preorder(self):
        """Returns a list containing the results of
        a preorder traversal."""
        # Exercise
        pass

    def postorder(self):
        """Returns a list containing the results of
        a postorder traversal."""
        # Exercise
        pass


    def levelorder(self):
        """Returns a list containing the results of
        a levelorder traversal."""
        # Exercise
        pass

    def remove(self, item):
        # Exercise
        pass

def main():
    tree = BST()
    print "Adding D B A C F E G"
    tree.add("D")
    tree.add("B")
    tree.add("A")
    tree.add("C")
    tree.add("F")
    tree.add("E")
    tree.add("G")

    print tree.find("A")
    print tree.find("Z")

    print "\nString:\n" + str(tree)

    print "Iterator (inorder traversal): "
    iterator = iter(tree)
    while True:
        try:
            print iterator.next(),
        except Exception, e:
            print e
            break
    
    # Use a for loop instead
    print "\nfor loop (inorder traversal): "
    for item in tree:
        print item,

if __name__ == "__main__":
    main()




