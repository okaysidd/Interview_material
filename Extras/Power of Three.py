"""
Power of Three
Given an integer, write a function to determine if it is a power of three.

Example 1:
Input: 27
Output: true

Example 2:
Input: 0
Output: false
"""
class Solution:
	"""
	3 ^ (log 3 MaxInt) = 3 ^ 19.56 = 3 ^ 19 = 1162261467
	Now Python does not have MaxInt anymore. But this is a good
	approach.
	"""
	def isPowerOfThree(self, n):
		return n > 0 and 1162261467 % n == 0

class Solution2:
	"""
	Convert to base 3. Powers of base 3 representation will have 1 followed
	by only 0s.
	"""
	def isPowerOfThree(self, n: int) -> bool:
		if n <= 0:
			return False
		res = self.toStr(n, 3)
		if str(res).replace('0', '') == '1':
			return True
		return False
		
	def toStr(self, n, base):
		convertString = "0123"
		if n < base:
			return convertString[n]
		else:
			return self.toStr(n//base,base) + convertString[n%base]

n = 45
x = Solution()
print(x.isPowerOfThree(n))
