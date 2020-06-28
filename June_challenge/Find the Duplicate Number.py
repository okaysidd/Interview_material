"""
Find the Duplicate Number
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:
Input: [1,3,4,2,2]
Output: 2

Example 2:
Input: [3,1,3,4,2]
Output: 3

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""
class Solution:
	"""
	Classic turtle and hare approach.
	First loop to find intersection.
	Second loop to find head/starting of the cycle.
	# NOTE: Same technique will be used to find start of cycle in a linked list.
	"""
	def findDuplicate(self, nums):
		slow = fast = nums[0]
		while True:
			slow = nums[slow]
			fast = nums[nums[fast]]
			if slow == fast:
				break
		slow = nums[0]
		while slow != fast:
			slow = nums[slow]
			fast = nums[fast]
		return slow

nums = [1,2,3,7,6,5,4,3,8,9,10]
x = Solution()
print(x.findDuplicate(nums))
