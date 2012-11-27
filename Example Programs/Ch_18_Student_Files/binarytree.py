"""
File: binarytree.py

A binary tree ADT

Example initializations:
anEmptyTree = BinaryTree.THE_EMPTY_TREE
aNonemptyTree = BinaryTree("One item")

"""

from queue import LinkedQueue

class EmptyTree(object):
    """Represents an empty tree."""

    # Supported methods

    def isEmpty(self):
        return True

    def __str__(self):
        return ""

    def __iter__(self):
        """Iterator for the tree."""
        return iter([])

    def preorder(self, lyst):
        return

    def inorder(self, lyst):
        return

    def postorder(self, lyst):
        return

    # Methods not supported but in the interface for all
    # binary trees

    def getRoot(self):
        raise AttributeError, "Empty tree"

    def getLeft(self):
        raise AttributeError, "Empty tree"
    
    def getRight(self):
        raise AttributeError, "Empty tree"

    def setRoot(self, item):
        raise AttributeError, "Empty tree"

    def setLeft(self, tree):
        raise AttributeError, "Empty tree"
    
    def setRight(self, tree):
        raise AttributeError, "Empty tree"

    def removeLeft(self):
        raise AttributeError, "Empty tree"
    
    def removeRight(self):
        raise AttributeError, "Empty tree"

class BinaryTree(object):
    """Represents a nonemoty binary tree."""

    # Singleton for all empty tree objects
    THE_EMPTY_TREE = EmptyTree()

    def __init__(self, item):
        """Creates a tree with
        the given item at the root."""
        self._root = item
        self._left = BinaryTree.THE_EMPTY_TREE
        self._right = BinaryTree.THE_EMPTY_TREE

    def isEmpty(self):
        return False

    def getRoot(self):
        return self._root

    def getLeft(self):
        return self._left
    
    def getRight(self):
        return self._right

    def setRoot(self, item):
        self._root = item

    def setLeft(self, tree):
        self._left = tree
    
    def setRight(self, tree):
        self._right = tree

    def removeLeft(self):
        left = self._left
        self._left = BinaryTree.THE_EMPTY_TREE
        return left
    
    def removeRight(self):
        right = self._right
        self._right = BinaryTree.THE_EMPTY_TREE
        return right

    def __str__(self):
        """Returns a string representation of the tree
        rotated 90 degrees to the left."""
        def strHelper(tree, level):
            result = ""
            if not tree.isEmpty():
                result += strHelper(tree.getRight(), level + 1)
                result += "| " * level
                result += str(tree.getRoot()) + "\n"
                result += strHelper(tree.getLeft(), level + 1)
            return result
        return strHelper(self, 0)

    def __iter__(self):
        """Iterator for the tree."""
        lyst = []
        self.inorder(lyst)
        return iter(lyst)

    def preorder(self, lyst):
        """Adds items to lyst during
        a preorder traversal."""
        lyst.append(self.getRoot())
        self.getLeft().preorder(lyst)
        self.getRight().preorder(lyst)

    def inorder(self, lyst):
        """Adds items to lyst during
        an inorder traversal."""
        self.getLeft().inorder(lyst)
        lyst.append(self.getRoot())
        self.getRight().inorder(lyst)

    def postorder(self, lyst):
        """Adds items to lystduring
        a postorder traversal."""
        self.getLeft().postorder(lyst)
        self.getRight().postorder(lyst)
        lyst.append(self.getRoot())

    def levelorder(self, lyst):
        """Adds items to lyst during
        a levelorder traversal."""
        levelsQueue = LinkedQueue()
        levelsQueue.enqueue(self)
        while not levelsQueue.isEmpty():
            node = levelsQueue.dequeue()
            lyst.append(node.getRoot())
            left = node.getLeft()
            right = node.getRight()
            if not left.isEmpty():
                levelsQueue.enqueue(left)
            if not right.isEmpty():
                levelsQueue.enqueue(right)
    


