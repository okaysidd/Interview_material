"""
231. Power of Two
Given an integer, write a function to determine if it is a power of two.

Example 1:
Input: 1
Output: true 
Explanation: 20 = 1

Example 2:
Input: 16
Output: true
Explanation: 24 = 16

Example 3:
Input: 218
Output: false
"""
class Solution:
	"""
	Trivial question but trick of (binary) & is important.
	A power of 2 will have binary format 100... Using this
	here.
	"""
	def isPowerOfTwo(self, n: int) -> bool:
		return n>0 and not (n & n-1)

n = 128
x = Solution()
print(x.isPowerOfTwo(n))
