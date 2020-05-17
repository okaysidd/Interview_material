"""
Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

class Solution:
	"""
	Brute force algorithm to find sum of all the sub arrays.
	"""
	def maxSubArray(self, nums):
		max_ = nums[0]
		for i in range(len(nums)):
			for j in range(i+1, len(nums)+1):
				max_ = max(max_, sum(nums[i:j]))
		return max_

a = Solution()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

class Solution2:
	"""
	Kadane's algorithm that takes linear time and no extra space.
	"""
	def maxSubArray(self, nums):
		max_, c = nums[0], 0
		for i in nums:
			c += i
			c = max(c, i)
			max_ = max(max_, c)
		return max_

a = Solution2()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
