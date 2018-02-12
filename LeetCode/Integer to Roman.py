"""
	Given an integer, convert it to a roman numeral.

	Input is guaranteed to be within the range from 1 to 3999.

	https://leetcode.com/problems/integer-to-roman/description/

	-- mzellhuber February 10, 2018

   (c) 2018 Melissa Zellhuber, All Rights Reserved.

"""


values = [[1000,"M"], [900,"CM"], [500,"D"], [400,"CD"], [100,"C"], [90,"XC"], [50,"L"], [40,"XL"], [10,"X"], [9,"IX"], [5,"V"], [4,"IV"], [1,"I"]]

def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """

    result = ""

    for n, r in values:
    	result+=r*(num/n)
    	num%=n

    return result


print(intToRoman(3999))