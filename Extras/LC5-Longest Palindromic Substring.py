"""
Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
"""
class Solution:
	"""
	Brute force would be checking all substrings if they are palindrome.
	Smarter way is to to expand at each index, towards left and right,
	to check if they have same characters around them (thus increasing
	the length of the palindrome string).
	The trick is that for odd length palidrome like 'aba', we expand from
	index 1 and get two a on both sides, thus increasing the length.
	However, for even length palindromes like abba, the center point
	is not an index but between two indicies, so we have to check those
	instances as well (comment marked below).
	"""
	def longestPalindrome(self, s: str) -> str:
		if len(s) == 0:
			return s
		max_ = max(self.helper(0, 0, s)[0], 0)
		res = self.helper(0, 0, s)[1]
		for i in range(1, len(s)):
			first = self.helper(i-1, i, s) # for abba cases
			second = self.helper(i, i, s) # for aba cases
			max_ = max(max_, first[0], second[0])
			if max_ == first[0]:
				res = first[1]
			if max_ == second[0]:
				res = second[1]
		return res
	def helper(self, i, j, s):
		if s[i] == s[j]:
			if i>0 and j<len(s)-1 and s[i-1] == s[j+1]:
				return self.helper(i-1, j+1, s)
			else:
				return len(s[i:j+1]), s[i:j+1]
		else:
			return len(s[i:j]), s[i:j]

s = 'cbbd'
x = Solution()
print(x.longestPalindrome(s))
