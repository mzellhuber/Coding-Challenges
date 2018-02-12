"""

	Find the total area covered by two rectilinear rectangles in a 2D plane.

	Each rectangle is defined by its bottom left corner and top right corner

	Assume that the total area is never beyond the maximum possible value of int.

	-- mzellhuber February 11, 2018

   (c) 2018 Melissa Zellhuber, All Rights Reserved.

"""

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Rectangle():
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2
		

def overlap(r1, r2):
	height = abs(min(r1.p2.y, r2.p2.y)-max(r1.p1.y, r2.p1.y))
	width = abs(min(r1.p2.x, r2.p2.x)-max(r1.p1.x, r2.p1.x))

	res = height*width

	return res


print overlap(Rectangle(Point(2,1), Point(5,5)),Rectangle(Point(3,2), Point(5,7)))