"""
Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
# NOTE: IMPORTANT!
"""
class Solution:
	"""
	Backtracking, keep count of left and right; there can be maximum n number of
	opening brackets. And same right. So if there are less than n opening brackets,
	add opening bracket to increase the pattern. If number of closing brackets are
	less than opening, add closing to the pattern.
	"""
	def generateParenthesis(self, n):
		result = []
		def backtrack(combination='', left=0, right=0):
			nonlocal n, result
			if len(combination) == 2 * n:
				result.append(combination)
			if left < n:
				backtrack(combination + '(', left + 1, right)
			if right < left:
				backtrack(combination + ')', left, right + 1)
		backtrack()
		return result

n = 3
x = Solution()
print(x.generateParenthesis(n))
