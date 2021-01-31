'''
**Question**: Given a Binary Search Tree, return the elements in order without using recursion.

**Explanation**: For the sake of the exercise I begin by implementing a Binary Search Tree.
A Binary Search Tree (or BST) is a binary tree where all nodes in the left subtree of a node N have
a value lower than N, and all the nodes in the right subtree have a higher value than N.

The class structure will be fairly simple. The class will keep a reference to only the root node,
each node will have two children, `left` and `right`.

```python
# For simplicity, every Node has its value as key.
class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        # Root will be added at first insertion.
        self.__root = None

    def add(self, value):
        # Add a value to the tree following the bst criteria.

    def remove(self, value):
        # Remove a value, looking it up with the bst criteria.

    def __contains__(self, value):
        # Find the value (override for `in` keyword).

    def __iter__(self):
        # The trasversal we are required to implement.

    def trasverse(tree):
        # Static version of the trasverse.
```

Traversal of a binary tree is quite trivial with recursion:

```python
def traverse_binary_tree(node, callback):
    if node == None:
        return
    traverse_binary_tree(node.leftChild, callback)
    callback(node.value)
    traverse_binary_tree(node.rightChild, callback)
```

But we are asked to do it iteratively. The algorithm requires us to:
1. Go "as far left as possible"
2. Go right once, repeat step 1
3. If cannot go right, go back to the parent, try again until you can go right.

An alternative solution involves a stack: when you visit a node, put its right child at the top of
the stack, then visit its left child. When no left child is found, pop the first node from the stack
and visit that one.

> **WARNING**: incomplete. Cuz it was hella boring honestly.
'''

__author__ = "Riccardo De Zen <riccardodezen98@gmail.com>"

from typing import Generic, TypeVar

T = TypeVar('T')
'''The generic type of data in the Tree's nodes (`value` attribute).'''


class TreeNode(Generic[T]):

    def __init__(self, value: T):
        '''
        Parameters:
            value : T
                The value for the Node.
        '''
        self.value: T = value
        self.left: TreeNode = None
        self.right: TreeNode = None


class BinarySearchTree(Generic[T]):

    '''
    Binary search tree class.
    '''

    def __init__(self, root: TreeNode[T] = None):
        '''
        Parameters:
            root : TreeNode[T]
                Optional root node.
        '''
        self.root = root

    def add(self, value: T):
        '''
        Add a value to the tree following the bst criteria.

        Parameters:
            value : T
                The value to insert.
        '''
        node = self.root
        while True:
            # Go to the left
            if value <= node.value:
                if node.left is None:
                    node.left = TreeNode(value)
                    break
                node = node.left
            # Go to the right
            else:
                if node.right is None:
                    node.right = TreeNode(value)
                    break
                node = node.right

    def remove(self, value: T) -> bool:
        '''
        Remove a value, looking it up with the bst criteria.

        Parameters:
            value : T
                The value to remove from the tree.

        Returns:
            bool : Whether the value was found and thus removed.
        '''
        parent = None
        child = -1
        node = self.root
        while node is not None:
            # Found the value. Remove it.
            # New node is any of the children of the removed node.
            if value == node.value:
                if node.left and node.right:
                    # The left child becomes the parent's child
                    parent.left = node.left

 #               else:

#                return True
            # Go left
            if value < node.value:
                parent = node
                child = 0
                node = node.left
            # Go right
            else:
                parent = node
                child = 1
                node = node.right
        # Node is null => The value is not in the tree.
        return False

    def __contains__(self, value: T):
        # Find the value (override for `in` keyword).
        pass

    def __iter__(self):
        # The trasversal we are required to implement.
        pass

    def trasverse(tree):
        # Static version of the trasverse.
        pass
