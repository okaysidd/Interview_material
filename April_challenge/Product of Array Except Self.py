"""
Product of Array Except Self
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.
Note: Please solve it without division and in O(n).
Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
class Solution:
	"""
	Since division is not allowed, create a new arrays L and R.
	L contains at each index, product of numbers on the left of that index.
	R contains at each index, product of numbers on the right of that index.
	Then use them to create answer array.
	O(n) but uses extra space.
	For using less space, create a R array (for instance) and keep calculating
	the product of left side numbers as you go on traversing the array.
	O(n) time and O(1) space, not counting output array.
	F*cking brilliant!
	"""
	def productExceptSelf(self, nums):
		R = [1]*len(nums)
		for i in range(len(nums)-2, -1, -1):
			R[i] = nums[i+1]*R[i+1]
		p = 1
		for i in range(len(nums)):
			x = nums[i]
			nums[i] = p * R[i]
			p *= x
		return nums

nums = [1,2,3,4]
a = Solution()
print(a.productExceptSelf(nums))
