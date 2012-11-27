"""
File: bst.py
BST and BTNode classes for binary search trees.
"""

from queue import LinkedQueue

class BTNode(object):

    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BST(object):

    def __init__(self):
        self._root = None
        self._size = 0

    def add(self, item):
        newNode = BTNode(item)

        # Tree is empty, so item goes at the root
        if self.isEmpty():
            self._root = newNode
            self._size += 1
            return None
 
        # Search for the item's spot or a duplicate
        else:
            probe = self._root
            while probe != None:

                # A duplicate is found, replace it and return it
                if item == probe.data:
                    oldData = probe.data
                    probe.data = item
                    return oldData

                # New item is less, go left until spot is found
                elif item < probe.data:
                    if probe.left != None:
                        probe = probe.left
                    else:
                        probe.left = newNode
                        self._size += 1
                        return None

                # New item is greater, go right until spot is found
                elif probe.right != None:
                    probe = probe.right
                else:
                    probe.right = newNode
                    self._size += 1
                    return None

    def find(self, item):
        """Returns data if item is found or None otherwise."""
        def findHelper(tree, item):
            if tree is None:
                return None
            elif item == tree.data:
                return tree.data
            elif item < tree.data:
                return findHelper(tree.left, item)
            else:
                return findHelper(tree.right, item)
        return findHelper(self._root, item)

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0


    def __iter__(self):
        return iter(self.inorderTraverse())

    def inorderTraverse(self):
        """Returns a list containing the results of
        an inorder traversal."""
        def inorderHelper(tree, lyst):
            if tree != None:
                inorderHelper(tree.left, lyst)
                lyst.append(tree.data)
                inorderHelper(tree.right, lyst)
        lyst = []
        inorderHelper(self._root, lyst)
        return lyst


    def preorderTraverse(self):
        """Returns a list containing the results of
        a preorder traversal."""
        def preorderHelper(tree, lyst):
            if tree != None:
                lyst.append(tree.data)
                preorderHelper(tree.left, lyst)
                preorderHelper(tree.right, lyst)
        lyst = []
        preorderHelper(self._root, lyst)
        return lyst

    def postorderTraverse(self):
        """Returns a list containing the results of
        a postorder traversal."""
        def postorderHelper(tree, lyst):
            if tree != None:
                postorderHelper(tree.left, lyst)
                postorderHelper(tree.right, lyst)
                lyst.append(tree.data)
        lyst = []
        postorderHelper(self._root, lyst)
        return lyst


    def levelorderTraverse(self):
        """Returns a list containing the results of
        a levelorder traversal."""
        def levelorderHelper(levelsQu, lyst):
            if not levelsQu.isEmpty():
                node = levelsQu.dequeue()
                lyst.append(node.data)
                if node.left != None:
                    levelsQu.enqueue(node.left)
                if node.right != None:
                    levelsQu.enqueue(node.right)
                levelorderHelper(levelsQu, lyst)
        lyst = []
        levelsQu = LinkedQueue()
        if self._root != None:
            levelsQu.enqueue(self._root)
            levelorderHelper(levelsQu, lyst)
        return lyst

    def remove(self, item):
        def liftMaxInLeftSubtreeToTop(top):
        # Replace top's data with the max data
        # in the left subtree
        # Pre:  top has a left child
        # Post: the maximum node in top's left subtree
        #       has been removed
        # Post: top.data = max value in top's left subtree
            parent = top
            currentNode = top.left
            while currentNode.right != None:
                parent = currentNode
                currentNode = currentNode.right
            top.data = currentNode.data
            if parent == top:
                top.left = currentNode.left
            else:
                parent.right = currentNode.left

        if self.isEmpty(): return None
        # Attempt to locate the node containing the item
        itemRemoved = None
        preRoot = BTNode(None, self._root, None)
        parent = preRoot
        direction = 'L'
        currentNode = self._root
        while currentNode != None:
            if currentNode.data == item:
                itemRemoved = currentNode.data
                break
            parent = currentNode
            if currentNode.data > item:
                direction = 'L'
                currentNode = currentNode.left
            else:
                direction = 'R'
                currentNode = currentNode.right
        # Return null if the item is absent
        if itemRemoved == None: return None
        # The item is present, so remove its node

        # Case 1: The node has a left and a right child
        #         Replace the node's value with the max value in the
        #         left subtree
        #         Delete the max node in the left subtree
        if currentNode.left != None \
           and currentNode.right != None:
            liftMaxInLeftSubtreeToTop(currentNode)
        else:
        # Case 2: the node has no left child
            if currentNode.left is None:
                newChild = currentNode.right
        # Case 3: the node has no right child
            else:
                newChild = currentNode.left
        # Case 2 & 3: tie the parent to the new child
        if direction == 'L':
            parent.left = newChild
        else:
            parent.right = newChild
        # All cases: Reset the root (if it hasn't changed no harm done)
        #            Decrement the collection's size counter
        #            Return the item
        self._root = preRoot.left
        self._size -= 1
        return itemRemoved

    def __str__(self):
        """Returns a string representation of the tree
        rotated 90 degrees to the left."""
        def strHelper(tree, level):
            result = ""
            if tree != None:
                result += strHelper(tree.right, level + 1)
                result += "| " * level
                result += str(tree.data) + "\n"
                result += strHelper(tree.left, level + 1)
            return result
        return strHelper(self._root, 0)

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

    print("\nPreorder traversal: ")
    lyst = tree.preorderTraverse()
    print lyst
      
    print "\nPostorder traversal: "
    lyst = tree.postorderTraverse()
    print lyst

    print "\nLevel order traversal: "
    lyst = tree.levelorderTraverse()
    print lyst

    print "\nRemovals: "
    for ch in xrange(ord('A'), ord('H')):
        print tree.remove(chr(ch)),
    print "\n\nEmpty:", tree.isEmpty()

if __name__ == "__main__":
    main()




