"""
Sequential Digits
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example 1:
Input: low = 100, high = 300
Output: [123,234]

Example 2:
Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 
Constraints:
10 <= low <= high <= 10^9
"""
class Solution:
	"""
	Generate all numbers which have increasing order of digits.
	"""
	def sequentialDigits(self, low, high):
		dp = [1,2,3,4,5,6,7,8,9]
		out = []
		while len(dp)>0 and dp[0] <= high:
			elem = dp.pop(0)
			if low <= elem <= high:
				out.append(elem)
			if elem % 10 < 9:
				dp.append(elem*10 + elem % 10 + 1)
		return out

low = 10
high = 100000
x = Solution()
print(x.sequentialDigits(low, high))
