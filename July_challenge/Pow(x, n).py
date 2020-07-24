"""
Pow(x, n)

Solution
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
# NOTE: IMPORTANT!
"""
class Solution:
	"""
	This is the way to do it.
	Things to keep in mind:
	- While dealing with negative numbers, use int(x / 2) and not x // 2
		>>> int(-7/2)
		-3             --> correct
		>>> -7 // 2
		-4
	- Set the value of temp earlier (lineA) so that it isn't calculated again and again
	"""
	def myPow(self, x: float, n: int) -> float:
		if n == 0:
			return 1
		temp = self.myPow(x, int(n/2)) # lineA
		if n % 2 == 0:
			return temp * temp
		else:
			if n < 0:
				return (temp * temp) / x
			else:
				return x * temp * temp

x = 2
n = -10
obj = Solution()
print(obj.myPow(x, n))
