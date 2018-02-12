"""
We're going to make our own Contacts application! The application must perform two types of operations:

	1. add name, where name is a string denoting a contact name. This must store name as a new contact in the application.
	2. find partial, where partial is a string denoting a partial name to search the application for. It must count the number of contacts starting with partial and print the count on a new line.

Given n sequential add and find operations, perform each operation in order.

Input Format

The first line contains a single integer, n, denoting the number of operations to perform. 
Each line i of the n subsequent lines contains an operation in one of the two forms defined above.

Constraints

	* 1<= n <= 10^5
	* 1<= |name| <= 21
	* 1<= |partial|<= 21

	* It is guaranteed that name and partial contain lowercase English letters only.
	* The input doesn't have any duplicate name for the add operation.

Output Format

	For each find partial operation, print the number of contact names starting with on a new line.

Sample Input
	4
	add hack
	add hackerrank
	find hac
	find hak

Sample Output
	2
	0

Explanation

	We perform the following sequence of operations:

	1. Add a contact named hack.
	2. Add a contact named hackerrank.
	3. Find and print the number of contact names beginning with hac. There are currently two contact names in the application and both of them start with hac, so we print  on a new line.
	4. Find and print the number of contact names beginning with hak. There are currently two contact names in the application but neither of them start with hak, so we print  on a new line.
"""

def notTrie():
	#This version works but times out with testcases
	n = int(raw_input().strip())
	contacts=[]
	for a0 in xrange(n):
	    op, contact = raw_input().strip().split(' ')

	    if op == 'add':
	    	contacts.append(contact)
	    elif op == 'find':
	    	result = ([c.startswith(contact) for c in contacts]).count(True)
	    	print result

#Implementation using Tires
class Trie(object):
    def __init__(self):
        self.root = TNode(None)
    
    def add(self, val):
        node = self.root
        nodes = [node]
        for char in val:
            if char not in node.children:
                node.children[char] = TNode(char)
            node = node.children[char]
            nodes.append(node)

        if not node.count:
            for n in nodes:
                n.count += 1
    
    def find(self, val):
        node = self.root
        for char in val:
            node = node.children.get(char)
            if not node:
                return None
        return node
            
class TNode(object):
    __slots__ = ('key', 'count', 'children')
    def __init__(self, key):
        self.key = key
        self.count = 0
        self.children = {}    

trie = Trie()

n = int(raw_input().strip())
for a0 in xrange(n):
    op, contact = raw_input().strip().split(' ')
    if op == 'add':
        trie.add(contact)
    elif op == 'find':
        node = trie.find(contact)
        if not node:
            print '0'
        else:
            print node.count