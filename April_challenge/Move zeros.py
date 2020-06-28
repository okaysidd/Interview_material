"""
Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
-You must do this in-place without making a copy of the array.
-Minimize the total number of operations.
"""

class Solution:
	def moveZeroes(self, nums):
		"""
		Slow way to do the thing, relies on the condition that non zeroes order be maintained
		and hence while moving zeroes takes extra caution.
		"""
		k, z_at_end, i = 0, 0, 0
		while i < len(nums) - z_at_end - 1 and k < len(nums):
			print(nums)
			k += 1
			if nums[i] == 0:
				z_at_end += 1
				j = i
				while j < len(nums) - z_at_end - 1:
					nums[j], nums[j+1] = nums[j+1], nums[j]
					j += 1
			else:
				i += 1
		return nums

# a = Solution()
# print(a.moveZeroes([0,0,1,0,2,3,0]))

class Solution2:
	"""
	Works faster by pulling non zeroes to front instead of moving zeroes to the end.
	This makes moving any zero occurance to swap with any non zero occurance, thus no need 
	for maintaining order of non zero, since they'll be pulled in correct order anyway.
	"""
	def moveZeroes(self, nums):
		first, second = 0, 1
		while first < second and second < len(nums):
			if nums[first] == 0 and nums[second] != 0:
				nums[first], nums[second] = nums[second], nums[first]
			elif nums[first] == 0 and nums[second] == 0:
				second += 1
				continue
			first += 1
			second += 1
		return nums

a = Solution2()
print(a.moveZeroes([0,0,1,0,2,3,0]))
