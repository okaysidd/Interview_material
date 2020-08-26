"""
Find All Duplicates in an Array
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[2,3]
"""
class Solution:
	"""
	Good question.
	Replace the numbers with the index, if they were at their index location.
	At the end, those not at the proper place, are the duplicate ones.
	The position they occupy also gives the answer to what numbers are missing.
	# NOTE: LINE A here will not work if the swap order was switched.
	nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i] # does not work
	"""
	def findDuplicates(self, nums):
		i = 0
		while i<len(nums):
			if i == nums[i]-1:
				i += 1
			else:
				if nums[i] == nums[nums[i]-1]:
					i += 1
				else:
					nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1] # LINE A
		out = []
		for i in range(len(nums)):
			if i != nums[i] - 1:
				out.append(nums[i])
		return out

class Solution2:
	"""
	Another good solution IF THE NUMBERS ARE ALL POSITIVE.
	Make the numbers at index of number starting from 0 index to negative.
	If same index asks to be turned negative twice, means that index number
	is duplicate.
	"""
	def findDuplicates(self, nums):
		out = []
		for i in range(len(nums)):
			index = abs(nums[i])
			if nums[index - 1] < 0:
				out.append(index)
			else:
				nums[index - 1] = nums[index - 1] * -1
		return out

nums = [4,3,2,7,8,2,3,1]
x = Solution()
print(x.findDuplicates(nums))
