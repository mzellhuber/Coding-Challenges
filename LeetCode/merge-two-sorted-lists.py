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


#expected output 1-1-2-3-4-4
print(mergeLists([1,2,4], [1,3,4]))