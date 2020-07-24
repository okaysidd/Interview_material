"""
Minimum Difference Between Largest and Smallest Value in Three Moves
Given an array nums, you are allowed to choose one element of nums and change it by any value in one move.
Return the minimum difference between the largest and smallest value of nums after perfoming at most 3 moves.

Example 1:
Input: nums = [5,3,2,4]
Output: 0
Explanation: Change the array [5,3,2,4] to [2,2,2,2].
The difference between the maximum and minimum is 2-2 = 0.

Example 2:
Input: nums = [1,5,0,10,14]
Output: 1
Explanation: Change the array [1,5,0,10,14] to [1,1,0,1,1]. 
The difference between the maximum and minimum is 1-0 = 1.

Example 3:
Input: nums = [6,6,0,1,1,4,6]
Output: 2

Example 4:
Input: nums = [1,5,6,14,15]
Output: 1
"""
class Solution:
	"""
	Since only three numbers can be changed, we:
	- either change all biggest
	- or change all smallest
	- or change 2 biggest and 1 smallest
	- or change 2 smallest and 1 biggest
	According to these changes, the new minimum difference will be one of-
	- all biggest: fourth last - first
	- all smallest: last - fourth
	- 2 biggest, 1 smallest: third last - second
	- 2 smallest, 1 biggest: second last - third
	"""
	def minDifference(self, nums):
		if len(nums)<=4:
			return 0
		nums.sort()
		out = min(-nums[0] + nums[-4],
				 -nums[1] + nums[-3],
				  -nums[2] + nums[-2],
				 -nums[3] + nums[-1])
		return out

nums = [82,81,95,75,20]
x = Solution()
print(x.minDifference(nums))
