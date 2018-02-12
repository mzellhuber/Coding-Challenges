# Python program to for tree traversals
 
# A class that represents an individual node in a
# Binary Tree
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
 
ino=[]
#Inorder (Left, Root, Right)
# A function to do inorder tree traversal
def printInorder(root):
 
    if root:
 
        # First recur on left child
        printInorder(root.left)
 
        # then print the data of node
        #print(root.val),
        ino.append(root.val)
 
        # now recur on right child
        printInorder(root.right)
 
 
post=[]
#Postorder (Left, Right, Root)
# A function to do postorder tree traversal
def printPostorder(root):
 
    if root:
 
        # First recur on left child
        printPostorder(root.left)
 
        # the recur on right child
        printPostorder(root.right)
 
        # now print the data of node
        #print(root.val),
        post.append(root.val)
 
 
# A function to do postorder tree traversal
pre=[]
#Preorder (Root, Left, Right)
def printPreorder(root):
 
    if root:
 
        # First print the data of node
        #print(root.val),
        pre.append(root.val)
 
        # Then recur on left child
        printPreorder(root.left)
 
        # Finally recur on right child
        printPreorder(root.right)
 
 
# Driver code
root = Node(1)
root.left      = Node(2)
root.right     = Node(3)
root.left.left  = Node(4)
root.left.right  = Node(5)
root.right.left = Node(7)
root.right.right = Node(6)
print "Preorder traversal of binary tree is"
printPreorder(root)
print(pre)
print "\nInorder traversal of binary tree is"
printInorder(root)
print(ino)
print "\nPostorder traversal of binary tree is"
printPostorder(root)
print(post)

def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i