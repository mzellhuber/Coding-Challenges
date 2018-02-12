# O(n) solution to find LCS of two given values n1 and n2
 
# A binary tree node
class Node:
    # Constructor to create a new binary node
    def __init__(self, key):
        self.key =  key
        self.left = None
        self.right = None
 

def findLCA(root, n1, n2):
    if root is None:
        return

    if root.key == n1 or root.key == n2:
        return root.key

    left = findLCA(root.left, n1, n2)
    right = findLCA(root.right, n1, n2)

    if left is not None and right is not None:
        return root.key

    if left is None and right is None:
        return

    if left is not None:
        return left
    else:
        return right



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
 
print "LCA(4, 5) = %d" %(findLCA(root, 4, 5,))
print "LCA(4, 6) = %d" %(findLCA(root, 4, 6))
print "LCA(3, 4) = %d" %(findLCA(root,3,4))
print "LCA(2, 4) = %d" %(findLCA(root,2, 4))
print "LCA(6, 7) = %d" %(findLCA(root,6, 7))