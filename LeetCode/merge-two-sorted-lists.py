"""
	Merge two sorted linked lists and return it as a new list. 
	The new list should be made by splicing together the nodes of the first two lists.

	Example:

	Input: 1->2->4, 1->3->4
	Output: 1->1->2->3->4->4


	https://leetcode.com/problems/merge-two-sorted-lists/description/

	-- mzellhuber April 27, 2018

   (c) 2018 Melissa Zellhuber, All Rights Reserved.

"""


"""Merge two sorted lists"""
def mergeLists(list1, list2):
	"""
	:type list1: [int], list2: [int]
	:rtype: [int]
	"""
	merged = []
	total = len(list1)+len(list2)

	while len(merged) < total:

		if len(list1) == 0:
			merged.append(list2[0])
			del list2[0]
		elif len(list2) == 0:
			merged.append(list1[0])
			del list1[0]
		elif list1[0] > list2[0]:
			merged.append(list2[0])
			del list2[0]
		else:
			merged.append(list1[0])
			del list1[0]

	return merged

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Linked List version

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None
		

def mergeListsLL(l1, l2):
	"""
	:type l1: ListNode
	:type l2: ListNode
	:rtype: ListNode
	"""
	if l1 and l2:
		if l1.val > l2.val:
			l1, l2 = l2, l1
		l1.next = mergeListsLL(l1.next, l2)

	return l1 or l2

#expected output 1-1-2-3-4-4
print(mergeLists([1,2,4], [1,3,4]))

#list 1
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)

#list 2
node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)


node1.next = node2
node2.next = node3

node4.next = node5
node5.next = node6

#expected output 1-1-2-3-4-4

node = mergeListsLL(node1, node4)
while node:
	print node.val
	node = node.next