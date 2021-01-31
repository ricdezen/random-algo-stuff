# Byte By Byte

Collection of coding interview problems found on [Byte by Byte](https://www.byte-by-byte.com/)

### **Priority Queue**

**Question**: Implement a Priority Queue.

**Explanation**:
- A Queue is a data structure comprised of mainly two methods: `push` and `pop`. The former inserts
  an element into the Queue, while the latter removes it and returns it.
- A Priority Queue guarantees the following:
    1. A pushed element can (must) be assigned a priority.
    2. The popped element will always be the one with the higher priority.

The most basic implementation involves having an array on which you insert elements, while
maintaining ordering over the priority. Every insertion and removal takes `O(n)` time. Removal can
be constant time if the array is managed as a circular queue.

A better implementation involves using a Heap, a binary tree where each node has a certain key, and
a node's children always have keys with a lower value.
A Heap can be easily implemented using an array where, given a node N and its index i, N's children
are situated at indexes 2\*i+1 and 2\*i+2.

Both the Priority Queue and the Heap can obviously be implemented to use min logic instead of max
logic.

### **Binary Search Tree**

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

### **Array Median**

**Question**: Find the median of two sorted arrays.

**Explanation**: Given an array of length `n`, its median is the `n/2` smallest element in the array
if `n` is odd, and the average of the `n/2` and `(n-1)/2` elements if `n` is even.
The two arrays are merged into one while keeping the ordering and then the median is computed on the
resulting array.

