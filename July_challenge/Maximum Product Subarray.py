"""
Maximum Product Subarray
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
class Solution:
	"""
	# NOTE: IMPORTANT - Good question!
	Since product can increase when two negatives come together so we maintain a
	minimum counter as well.
	"""
	def maxProduct(self, nums):
		prev_max, prev_min, cur_max, cur_min, res = nums[0], nums[0], nums[0], nums[0], nums[0]
		for i in range(1, len(nums)):
			cur_min = min(prev_max*nums[i], prev_min*nums[i], nums[i])
			cur_max = max(prev_max*nums[i], prev_min*nums[i], nums[i])
			res = max(res, cur_max)
			prev_min = cur_min
			prev_max = cur_max
		return res

nums = [2,3,-2,4]
x = Solution()
print(x.maxProduct(nums))
