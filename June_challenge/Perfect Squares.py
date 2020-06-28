"""
Perfect Squares
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
# NOTE: IMPORTANT!
"""
import math
class Solution:
	"""
	Required knowledge of a mathematical proof:
	https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem
	- all integers can be represented as sum of squares of four other integers
		n = x1^2 + x2^2 + x3^2 + x4^2 (one or more of x values may be 0 or 1. 
		So effectively, anywhere between 1 and 4.)
	- we can check the possibility of 1 by checking it for a perfect square.
	- we can check possibility of 2 by checking each number, say a and checking if
		a^2 and n-a^2 sum up to make n
	- we skip checking for three
	- we can check for 4 by: a number can be expressed as sum of squares of 3 other integers
		if and only if it (the number) is not of the form (4^k)*(8*m + 7). If this checks out,
		answer is four, else answer is last resort - 3.
	We do this in the order of check for 4, then 1 then 2 then 3, to avoid unnecessary
	computation while checking for others.
	"""
	def numSquares(self, n: int) -> int:
		while n%4 == 0: # divide continously by 4 to eliminate the 4^k term
			n /= 4
		if n%8 == 7:
			return 4
		a = 0
		while a*a <= n:
			b = int(math.sqrt(n - a*a))
			if a*a + b*b == n:
				return (not not a) + (not not b)  
			a = a + 1
		return 3

class Solution2:
	"""
	Classic dynamic programming solution.
	We create dp list with all values in list equal to index.
	We know values for n={0,1,2,3}.
	For every dp[i] from 4 to n, we need a loop to check if there is
	a perfect sqaure that can be subtracted from it to get a lower number. 
	"""
	def numSquares(self, n):
		dp = [x for x in range(n+1)]
		if n in {0,1,2,3}:
			return n
		i = 2
		for i in range(4, len(dp)):
			j = 2
			while j*j <= i:
				# print(i, j)
				dp[i] = min(dp[i], 1+ dp[i-(j*j)])
				j += 1
		return dp[-1]

n = 71
x = Solution()
print(x.numSquares(n))
