"""
	An ordinal number is a word representing rank or sequential order. The naming convention for royal names is to follow a first name with an ordinal number, which is essentially a Roman numeral used to indicate the birth order of two people having the same name. The roman numerals from 1 to 50 are defined as follows:

	-The respective numerals corresponding to numbers 1 through 10 are I, II, III, IV, V, VI, VII, VIII, IX and X.
	-The respective numerals corresponding to the numbers 20, 30, 40, and 50 are XX, XXX, XL and L
	-The numeral for any other two-digit number < 50 is constructed by concatenating the numeral(s) for its multiples of ten with the numeral(s) for its values < 10. For example, 47 is 40+7 = "XL"+"VII" = "XLVII".
		
	Example:

		Richard IV. The Roman numeral in the title can go 
		to L (50). You are given the Roman numerals from 1 to 10:
		I II III IV V VI VII VIII IX X. And you are given the 10 
		multiples up to 50: XX XXX IL L. Numbers between 10 and 50 
		that are not given can be formed from 10 multiples and a 
		numeral b/w 1 and 9. Example: 48 is XLVIII which is XL (40) 
		plus VIII (8).
		
	You are given an array of Roman titles sort it as follows: 
	sort it on the name unless the names are equal, in which
	case you have to sort it on the ordinal of the numerals.

	Examples:

		Henry II, Edward VIII => Edward VII, Henry II
		Richard V, Richard II, Richard X => Richard II, 
      Richard V, Richard X

   -- mzellhuber January 29, 2018

   (c) 2018 Melissa Zellhuber, All Rights Reserved.
"""

names = ["Edward VII","Richard II","Richard III", "Henry II","Richard X","Albert II","Polo IV","Alexander V","Elizabeth XXV","Albert XL","Polo XLVI","William IX","Edward XXXIX","Elizabeth XIX"]

class Royal:
	def __init__(self, name, rankR, rankA):
		self.name = name
		self.rankR = rankR
		self.rankA = rankA

	def __str__(self):
		string = self.name +" "+ str(self.rankA)
		return str(string)

def sortRoyalNames(names):
	royals = []
	for x in xrange(0,len(names)):
		line = names[x].split()
		name = line[0]
		rankA = line[1]
		rankR = romanToDec(rankA)

		r = Royal(name, rankR, rankA)

		royals.append(r)

	royals = sorted(royals, key=lambda x: (x.name, x.rankA))

	for r in royals:
		print str(r)


"""Convert from Roman numerals to Decimal."""
def romanToDec(string):
	values={'M': 1000, 'D': 500, 'C': 100, 'L': 50,'X': 10, 'V': 5, 'I': 1}

	total = 0
	while string:
		if len(string) == 1 or values[string[0]] >= values[string[1]]:
			total += values[string[0]]
			string = string[1:]
		else:
			total += values[string[1]] - values[string[0]]
			string = string[2:]

	return total

sortRoyalNames(names)