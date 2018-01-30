"""
	-Splitting Pixels-
	Consider a sequence of 24 bits defining a pixel, where the leftmost 8 bits describe its red component, the middle 8 bits describe its green component and the rightmost 8 bits describe its blue component. The pizel's red, green, and blue components are in the inclusive range from decimal 0 (binary 00000000) to decimal 255 (binary 11111111).

	We want to determine whether the pixel's color is geometrically closest to pure red, green, blue, white, or black. The formula for calculating the geometric distance between two colors with RGB components(r2,g2,b2) is:

		d=sqrt((r1-r2)^2+(g1-g2)^2+(b1-b2)^2)

	For reference, we define the following RGB values:

		+-----------------+---------------+
		| Pure Color Name |   RGB Value   |
		+-----------------+---------------+
		| Black           | (0,0,0)       |
		| White           | (255,255,255) |
		| Red             | (255,0,0)     |
		| Green           | (0,255,0)     |
		| Blue            | (0,0,255)     |
		+-----------------+---------------+

	Given a 24-bit binary string discribing a pixel, we want to identify which of these five colors the pixel is closest to (i.e., which pure color has the smallest Euclidean distance from the pixel). We then choose one of the following six answers:

	* Red if the pixel is closest to pure red
	* Green if the pixel is closest to pure green
	* Blue if the pixel is closest to pure blue
	* Black if the pixel is closest to pure black
	* White if the pixel is closest to pure white
	* Ambiguous if the pixel is equally closest to two or more colors.

	Example:

	The function takes one parameter, an array of 24-bit binary strings describing the pixel's respective 8-bit red, green, and blue values.

	The function must return an array of strings where each index i contains the answer for pixels. Note that these answers are case-sensitive and must be in the set of ("Red", "Green", "Blue", "Black", "White", "Ambiguous").

	-Input format
		Each line i of the n subsequent lines contains a 24-bit binary string describing pixels

	-Output Format
		Return an array of strings where each index i contains the answer for pixels.

	-Sample Case 0
		*Sample Input
			101111010110011011100100
			110000010101011111101111
			100110101100111111101101
			010111011010010110000011
			000000001111111111111111

		*Sample Output
			White
			White
			White
			Green
			Ambiguous

	-Explanation
		We process the following n = 5 binary strings:

		0. 101111010110011011100100 -> (189,102,228) is closest to White:
			* The distance to pure White is 168.80165875962237
			* The distance to pure Blue is 216.45784809056934
			* The distance to pure Red is 258.3486016993318
			* The distance to pure Black is 313.22356233208257
			* The distance to pure Green is 333.33766663850037


   -- mzellhuber January 29, 2018

   (c) 2018 Melissa Zellhuber, All Rights Reserved.
"""
import math

pixels = ["101111010110011011100100", "110000010101011111101111","100110101100111111101101", "010111011010010110000011","000000001111111111111111"]

class Color:
	def __init__(self, red, green, blue):
		self.red = red
		self.green = green
		self.blue = blue

WHITE = Color(255,255,255)
BLACK = Color(0,0,0)
RED = Color(255,0,0)
GREEN = Color(0,255,0)
BLUE = Color(0,0,255)

colors = [WHITE, BLACK, RED, GREEN, BLUE]
colorNames = ["White", "Black", "Red", "Green", "Blue"]

def getDistance(c1,c2):

	d = math.sqrt(math.pow((c1.red-c2.red),2)+math.pow((c1.green-c2.green),2)+math.pow((c1.blue-c2.blue),2))

	return d

def splittingPixels(pixels):
	results = []

	for pixel in pixels:
		distances = {}

		red = int(pixel[0:8],2)
		green = int(pixel[8:16],2)
		blue = int(pixel[16:24],2)

		x = Color(red, green, blue)

		for i in range(0, len(colors)):
			distances[colorNames[i]]=getDistance(x, colors[i])

		distances = sorted(distances.items(), key=lambda x: x[1])

		if distances[0][1] == distances[1][1]:
			results.append('Ambiguous')
		else:
			results.append(distances[0][0])
				
	return results

print splittingPixels(pixels)