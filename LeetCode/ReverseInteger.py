"""

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""

import sys

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x=str(x)
        i = 0
        sign = ''
        if x[0] in ['-', '+']:
            sign=x[0]
            if sign is '-':
                i= int(x[:0:-1])*-1
            else:
                i= int(x[:0:-1])
        else:
            i= int(x[::-1])
            
        return i if i.bit_length() < 32 else 0