"""
Longest Common Subsequence
Given two strings text1 and text2, return the length of their longest common subsequence.
A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.
If there is no common subsequence, return 0.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:
1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.
"""
class Solution:
	"""
	Using dynamic programming, creates a grid and traverses through the grid from
	top left to bottom right. If the characters at the current intersection match,
	add one to the top left diagonal and enter at the current square. Else, take
	max from the top or left and copy it here.
	Awesome.
	NOTE: Thing to remember, always create a grid with list comprehension, or loops,
	do not copy one list full of zeros over x number of times as they will hold the
	same memory location and will get affected as you alter one of them.!!!
	"""
	def longestCommonSubsequence(self, text1, text2, memo = None):
		text1 = ' ' + text1
		text2 = ' ' + text2
		grid = [[0 for i in range(len(text2))] for j in range(len(text1))] # important
		# as opposed to 
		# grid1 = [[0]*len(text2)]*len(text1)
		# memory location remains same for the copied lists.
		for i in range(1, len(text1)):
			for j in range(1, len(text2)):
				if text1[i] == text2[j]:
					grid[i][j] = grid[i-1][j-1] + 1
				else:
					grid[i][j] = max(grid[i-1][j], grid[i][j-1])
		return grid[-1][-1]

text1 = "ylqpejqbalahwr"
text2 = "yrkzavgdmdgtqpgf"
text1 = "pmjghexybyrgzczy"
text2 = "hafcdqbgncrcbihkd"
text1 = "abc"
text2 = "abcde"
# text1 = "bl"
# text2 = "yby"

a = Solution()
print(a.longestCommonSubsequence(text1, text2))


class Solution2:
	"""
	Slow way, uses recursion, and memoization is mandatory for any string
	even length >15. Is a valid way, just a very slow one. Not recommended.
	"""
	def longestCommonSubsequence(self, text1: str, text2: str, memo = None) -> int:
		if memo == None:
			memo = {}
		if (text1, text2) in memo.keys():
			return memo[(text1, text2)]
		if len(text1) == 0 or len(text2) == 0:
			return 0
		elif text1[0] == text2[0]:
			memo[(text1, text2)] = 1+self.longestCommonSubsequence(text1[1:], text2[1:], memo)
			return memo[(text1, text2)]
		else:
			memo[(text1, text2)] = max(self.longestCommonSubsequence(text1[1:], text2, memo), \
					self.longestCommonSubsequence(text1, text2[1:], memo))
			return memo[(text1, text2)]

text1 = "ylqpejqbalahwr"
text2 = "yrkzavgdmdgtqpgf"
text1 = "pmjghexybyrgzczy"
text2 = "hafcdqbgncrcbihkd"
text1 = "abc"
text2 = "abcde"
# text1 = "bl"
# text2 = "yby"

a = Solution2()
print(a.longestCommonSubsequence(text1, text2))
