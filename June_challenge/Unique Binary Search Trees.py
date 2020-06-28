"""
Unique Binary Search Trees
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:
# NOTE: IMPORTANT.
Catalan's number (formula)
Cn+1 = sum(Ci * Cn-i), i from [0->n]
Cn = sum(Ci * Cn-i-1), i from [0->n)
Cn = (fact(2*n)) / (fact(n+1) * n!)
https://en.wikipedia.org/wiki/Catalan_number
Places this will be used:
- Count number of BST with n nodes.
- Count number of expressions containing n pairs of parentheses which are correctly matched.
"""
class Solution:
	"""
	DP approach with dp table and bottoms up solution.
	"""
	def numTrees(self, n: int) -> int:
		dp = [0 for _ in range(n+1)]
		dp[0] = dp[1] = 1
		for i in range(2, n+1):
			for j in range(0, i):
				dp[i] += dp[j] * dp[i-j-1]
		return dp[n]

class Solution2:
	"""
	DP approach with recursion and memoization.
	"""
	def numTrees(self, n, memo=None):
		if memo == None:
			memo = {0:1, 1:1}
		if n in memo:
			return memo[n]
		res = 0
		for i in range(0, n):
			memo[i] = self.numTrees(i, memo)
			memo[n-i-1] = self.numTrees(n-i-1, memo)
			res += memo[i] * memo[n-i-1]
		return res

import math
class Solution3:
	"""
	Maths solution.
	"""
	def numTrees(self, n):
		return int((math.factorial(2*n)) / (math.factorial(n+1) * math.factorial(n)))

n = 400
x = Solution3()
print(x.numTrees(n))
