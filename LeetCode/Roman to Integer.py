"""
	Given a roman numeral, convert it to an integer.

	Input is guaranteed to be within the range from 1 to 3999.

	https://leetcode.com/problems/roman-to-integer/description/

	-- mzellhuber February 10, 2018

   (c) 2018 Melissa Zellhuber, All Rights Reserved.

"""


"""Convert from Roman numerals to Decimal."""
def romanToDec(s):
	"""
    :type s: str
    :rtype: int
    """
	values={'M': 1000, 'D': 500, 'C': 100, 'L': 50,'X': 10, 'V': 5, 'I': 1}

	total = 0

	while s:
		print total
		print s
		if len(s)==1 or (values[s[0]] >= values[s[1]]):
			total+=values[s[0]]
			s = s[1:]
		else:
			total+=(values[s[1]]-values[s[0]])
			s =s[2:]

	print total


romanToDec("MMMCMXCIII")