"""
198. House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""
"""
# NOTE: This is a dp problem, will be solved using a dp list with length
n + 1. The second method is effectively the same that uses two variables
that store the prev and prev-1 values instead of using space O(n).
!!!IMPORTANT QUESTION!!!
"""
class Solution1:
	"""
	At each step, we can pick the last max seen or the last-1 max seen
	plus the current number. dp list achieves just that.
	"""
	def rob(self, nums) -> int:
		if len(nums) == 0:
			return 0
		dp = [0]*(len(nums)+1)
		dp[0] = 0 # for 0 house, this is the amount that can be stolen
		dp[1] = nums[0] # for 1 house, the first house can only be stolen
		for i in range(1, len(nums)):
			dp[i+1] = max(dp[i-1]+nums[i], dp[i])
		return dp[-1]

class Solution2:
	"""
	At each step, we can pick the last max seen or the last-1 max seen
	plus the current number. prev_max and cur_max are used to achieve that.
	"""
	def rob(self, nums) -> int:
		if len(nums) == 0:
			return 0
		prev_max = 0
		cur_max = nums[0]
		m = cur_max
		for i in range(1, len(nums)):
			m = max(prev_max + nums[i], cur_max)
			prev_max = cur_max
			cur_max = m
		return m
	
	def rob_new(self, nums): # just more compact
		try:
			prev = 0
			current = new_val = nums[0]
			for i in range(1, len(nums)):
				new_val = max(prev+nums[i], current)
				prev, current = current, new_val
			return current
		except:
			return 0

	def rob_new2(self, nums):
		prev, current = 0, 0
		for i in range(len(nums)):
			prev, current = current, max(current, prev+nums[i])
		return current

class Solution3:
	def rob(self, nums):
		prev_max = 0
		current_max = 0
		for i in range(len(nums)):
			temp = prev_max
			prev_max = current_max
			current_max = max(current_max, temp + nums[i])
		return current_max

nums = [2,7,9,3,100]
x = Solution1()
print(x.rob(nums))
