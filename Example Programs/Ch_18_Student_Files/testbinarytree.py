"""
File: testbinarytree.py

Builds a full binary tree with 7 nodes.
"""

from binarytree import BinaryTree

# Create initial leaf nodes
a = BinaryTree("A")
b = BinaryTree("B")
c = BinaryTree("C")
d = BinaryTree("D")
e = BinaryTree("E")
f = BinaryTree("F")
g = BinaryTree("G")

# Build the tree from the bottom up, where
# d is the root node of the entire tree

# Build and set the left subtree of d
b.setLeft(a)
b.setRight(c)
d.setLeft(b)

# Build and set the right subtree of d
f.setLeft(e)
f.setRight(g)
d.setRight(f)

def size(tree):
    if tree.isEmpty():
        return 0
    else:
        return 1 + size(tree.getLeft()) + size(tree.getRight())

def frontier(tree):
    """Returns a list containing the leaf nodes
    of tree."""
    if tree.isEmpty():
        return []
    elif tree.getLeft().isEmpty() and tree.getRight().isEmpty():
        return [tree.getRoot()]
    else:
        return frontier(tree.getLeft()) + frontier(tree.getRight())

print "Size:", size(d)

print "String:"
print d

print "Frontier:", frontier(d)

print "Preorder:"
lyst = []
d.preorder(lyst)
print lyst

print "Inorder:"
lyst = []
d.inorder(lyst)
print lyst

print "Postorder:"
lyst = []
d.postorder(lyst)
print lyst

print "Levelorder:"
lyst = []
d.levelorder(lyst)
print lyst

print "Iterator:"
for item in d: print item,

print "Testing an exception:"
t = a.getLeft()
print "True:", t.isEmpty()
t.setRoot("An item")


    
