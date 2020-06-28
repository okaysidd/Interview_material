"""
Power of Two
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
	Simple question, but this trick makes it calculate very fast.
	Power of two numbers have a quality in their binary representation,
	that they are 1 and all 0s.
	"""
	def isPowerOfTwo(self, n: int) -> bool:
		return n>0 and not (n & n-1)

n = 8888
x = Solution()
print(x.isPowerOfTwo(n))
