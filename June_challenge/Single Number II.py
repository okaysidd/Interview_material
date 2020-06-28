"""
Single Number II
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,3,2]
Output: 3

Example 2:
Input: [0,1,0,1,0,1,99]
Output: 99
"""
class Solution:
	"""
	Really nice way to solve it.
	Using dict is the brute force way to go.
	This method sorts (nlogn), then compares  at every i, i+3,,. and so on,
	if the number at i-1 matches if it does not, that's the single number.
	nums = [1,4,4,4,5,5,5,1,3,1,2,3]
						 |<- partition one
	After sort: [1, 1, 1,| 2, 3, 3, 4, 4, 4, 5, 5, 5]
					i	 |    i <- this will not match with i-1
	"""
	def singleNumber(self, nums):
		nums.sort()
		if len(nums) == 1:
			return nums[0]
		if nums[-1] != nums[-2]:
			return nums[-1]
		i = 1
		while i + 1 < len(nums):
			if nums[i] != nums[i-1]:
				return nums[i-1]
			i += 3

nums = [1,4,4,4,5,5,5,1,3,1,2,3]
x = Solution()
print(x.singleNumber(nums))
