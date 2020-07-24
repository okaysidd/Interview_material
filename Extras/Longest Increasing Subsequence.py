"""
Longest Increasing Subsequence
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:
There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

This is essentially asking if the array was sorted, how many numbers were already in correct position relative to each other.
Thus it can be solved by creating duplicate list, taking set, sorting it and basically finding longest common subsequence with the original list.
But it is very slow.
"""
class Solution:
	"""
	For every i, find the longest subsequence till that index.
	"""
	def lengthOfLIS(self, nums):
		if len(nums)<1:
			return 0
		dp = [1]*len(nums)
		for i in range(len(nums)):
			for j in range(i):
				if nums[i] > nums[j]:
					dp[i] = max(dp[i], 1+dp[j])
		return max(dp)

nums = [10,9,2,5,3,7,101,18]
x = Solution()
print(x.lengthOfLIS(nums))

class Solution2:
	"""
	Using Longest common subsequence.
	"""
	def lengthOfLIS(self, nums):
		return self.LCS(nums, sorted(list(set(nums))))
	def LCS(self, nums1, nums2):
		nums1 = [0] + nums1
		nums2 = [0] + nums2
		grid = [[0 for x in range(len(nums2))] for y in range(len(nums1))]
		for i in range(1, len(grid)):
			for j in range(1, len(grid[0])):
				if nums1[i] == nums2[j]:
					grid[i][j] = 1 + grid[i-1][j-1]
				else:
					grid[i][j] = max(grid[i-1][j], grid[i][j-1])
		return grid[-1][-1]
