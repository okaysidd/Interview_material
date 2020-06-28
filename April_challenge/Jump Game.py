"""
Jump Game
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example 1:
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
jump length is 0, which makes it impossible to reach the last index.
"""
class Solution:
	"""
	Really awesome approach that works on the understanding that if we move
	from the right, we only have to find if we can reach the current position.
	And move backwards from there. If we cannot find a previous index that can
	help us reach the current right most position, we do not update the last
	element position.
	Love it.
	"""
    def canJump(self, nums):
        last = len(nums)-1
        index = last - 1
        while index >= 0 and last > 0:
            if index + nums[index] >= last:
                last = index
            index -= 1
        return last==0

a = Solution()
nums = [3,2,1,0,4]
print(a.canJump(nums))
