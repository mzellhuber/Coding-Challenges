# -*- coding: utf-8 -*-
"""
	Longest Common Prefix

	Write a function to find the longest common prefix string amongst an array of strings.

	https://leetcode.com/problems/longest-common-prefix/description/

	-- mzellhuber February 10, 2018

   (c) 2018 Melissa Zellhuber, All Rights Reserved.
"""
strs = ["geeksforgeeks", "geeks", "geek", "geezer"]

def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        res = ''
        for i in xrange(len(strs[0])):
            for j in xrange(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

print(longestCommonPrefix(strs))