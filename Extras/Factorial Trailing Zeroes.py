"""
172. Factorial Trailing Zeroes
Given an integer n, return the number of trailing zeroes in n!.

Example 1:
Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
"""
class Solution:
	"""
	Why does it work? We get a trailing zero from every encounter
	of 10 and 5. So integer division by 5 seems reasonable. But only
	for numbers under 25. Since 25 has factors 5, 5, this has to be
	taken into account. Same for 125, 625, etc.
	"""
	def trailingZeroes(self, n):
		x = 5
		res = 0
		while x <= n:
			res += n // x
			x *= 5
		return res

n = 9022
x = Solution()
print(x.trailingZeroes(n))
