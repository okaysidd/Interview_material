"""
Single Number III
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
Example:
Input:  [1,2,1,3,2,5]
Output: [3,5]
Note:
The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
"""
class Solution:
	"""
	Since all numbers are present twice, and two are present once, the XOR
	of the complete list will give us the XOR of these two numbers that are
	present once.
	We use a trick to find out the lowest set bit in this result and that bit will
	be set in one of the numbers and unset in another. Similarly that bit will be set
	for one group of numbers, and unset for other group. We use this to segregate
	the numbers in two groups by distributing them if the number & lowest_bit gives
	0 or gives 1.
	Once we segregate, it is Single Number I problem again, we do XOR all to find the
	one that is extra in its group.
	"""
	def singleNumber(self, nums):
		e = 0
		for i in nums:
			e ^= i
		low_bit = e & (-e)
		res = [0, 0]
		for i in nums:
			if low_bit & i:
				res[0] ^= i
			else:
				res[1] ^= i
		return res

class Solution2:
	def singleNunber(self, nums):
		d = {}
		for i in nums:
			if i in d:
				d[i] += 1
			else:
				d[i] = 1
		return [x for x in d.keys() if d[x] == 1]

nums = [1,2,1,3,2,5]
x = Solution()
print(x.singleNumber(nums))
