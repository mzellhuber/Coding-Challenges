"""
For the purposes of this challenge, we define a binary search tree to be a binary tree with the following ordering properties:

The data value of every node in a node's left subtree is less than the data value of that node.
The data value of every node in a node's right subtree is greater than the data value of that node.
Given the root node of a binary tree, can you determine if it's also a binary search tree?

Complete the function in your editor below, which has  parameter: a pointer to the root of a binary tree. It must return a boolean denoting whether or not the binary tree is a binary search tree. You may have to write one or more helper functions to complete this challenge.

Note: We do not consider a binary tree to be a binary search tree if it contains duplicate values.

Input Format

You are not responsible for reading any input from stdin. Hidden code stubs will assemble a binary tree and pass its root node to your function as an argument.

	*Example
		2
		1 2 3 4 5 6 7

Constraints

0 <= data <= 10^4

Output Format

You are not responsible for printing any output to stdout. Your function must return true if the tree is a binary search tree; otherwise, it must return false. Hidden code stubs will print this result as a Yes or No answer on a new line.
"""

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Returns true if the given tree is a binary search tree
def checkBST(root):
    return checkBSTUtil(root,-float('inf'), float('inf'))

# Return true if the given tree is a BST and its values
# >= min and <= max
#Keeps track of min and max of the tree
def checkBSTUtil(root, min_, max_):
    #Empty returns True
    if root is None:
        return True
    
    #Check if node is in the right positions with min and max
    if root.data < min_ or root.data > max_:
        return False

	#Check node subtree, update min and max
    return (checkBSTUtil(root.left, min_, root.data-1) and (checkBSTUtil(root.right, root.data+1, max_)))