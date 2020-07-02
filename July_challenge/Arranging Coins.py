"""
Arranging Coins
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
Given n, find the total number of full staircase rows that can be formed.
n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:
n = 5
The coins can form the following rows:
¤
¤ ¤
¤ ¤
Because the 3rd row is incomplete, we return 2.

Example 2:
n = 8
The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤
Because the 4th row is incomplete, we return 3.
"""
class Solution:
	"""
	Recursive solution, slow af.
	"""
	def arrangeCoins(self, n: int, i=1) -> int:
		if n < i or i <= 0:
			return 0
		return 1 + self.arrangeCoins(n-i, i+1)

import math
class Solution2:
	"""
	Formula with Binary search, faster.
	"""
	def arrangeCoins(self, n: int) -> int:
		l = 0
		r = n // 2 + 1
		while l <= r:
			mid = (l + r) // 2
			if math.ceil((mid*(mid+1))/2) == n:
				return mid
			if math.ceil((mid*(mid+1))/2) < n:
				l = mid+1
			else:
				r = mid-1
		return r

n = 180
x = Solution()
print(x.arrangeCoins(n))
