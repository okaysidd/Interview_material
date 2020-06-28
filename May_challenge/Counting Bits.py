"""
Counting Bits
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:
Input: 2
Output: [0,1,1]

Example 2:
Input: 5
Output: [0,1,1,2,1,2]
"""
import math

class Solution:
	"""
	Instead of counting 1s in all converted binary numbers, detect
	pattern that has one extra 1 from the previous pattern and use
	that.
	"""
	def countBits(self, num: int):
		res = [(0,0), (1,1), (2,1), (3,2)]
		two = 2
		if num<=3:
			return [i[1] for i in res[:num+1]]
		for i in range(4, num+1):
			if str(math.log2(i)).split('.')[1] == '0':
				two += 1
			u = 2**two
			res.append((i, res[i-u][1]+1))
		return [i[1] for i in res]

num = 5
x = Solution()
print(x.countBits(num))
