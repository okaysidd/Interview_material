"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.
How many possible unique paths are there?

Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:
Input: m = 7, n = 3
Output: 28
"""
class Solution:
	"""
	Dynamic programming using Bottom-up approach.
	Recursion with memoization.
	"""
	def uniquePaths(self, m: int, n: int, memo=None) -> int:
		if memo==None: memo={}
		if (m,n) in memo:
			return memo[(m,n)]
		if m<=0 or n<=0:
			return 0
		if m == 1 and n == 1:
			return 1
		else:
			memo[(m-1,n)] = self.uniquePaths(m-1, n, memo)
			memo[(m,n-1)] = self.uniquePaths(m, n-1, memo)
			return memo[(m-1, n)] + memo[(m, n-1)]

class Solution2:
	"""
	Dynamic programming using Top-down approach.
	DP table.
	"""
	def uniquePaths(self, m: int, n: int) -> int:
		dp = [[1 for x in range(m)] for y in range(n)]
		for i in range(1, len(dp)):
			for j in range(1, len(dp[0])):
				dp[i][j] = dp[i-1][j] + dp[i][j-1]
		return dp[-1][-1]

class Solution3:
	"""
	DP table that uses only 2 lists, not the complete matrix.
	"""
	def uniquePaths2(self, m, n):
		dp1 = dp2 = [1 for x in range(m)]
		for i in range(n-1):
			for j in range(1, len(dp1)):
				dp2[j] = dp2[j-1] + dp1[j]
			dp1 = dp2
			dp2 = [1 for x in range(m)]
		return dp1[-1]

m = 100
n = 100
x = Solution()
print(x.uniquePaths(m, n))
