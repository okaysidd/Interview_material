"""
3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution:
	"""
	Fix a number, perform 2Sum on rest, sorted list will let us use left/right
	method to do 2Sum. Avoiding duplicates is the main part.
	3Sum is better than 2Sum anyway.
	"""
	def threeSum(self, nums):
		if len(nums) <= 2:
			return []
		nums.sort()
		i = 0
		res = []
		for i in range(len(nums)-2):
			if i>0 and nums[i]==nums[i-1]: continue
			l = i+1
			r = len(nums)-1
			while l<r: # using left/right pointer method on sorted array to find 2Sum
				if nums[l]+nums[r] == -1*(nums[i]):
					res.append([nums[i], nums[l], nums[r]])
					while l<r and nums[l]==nums[l+1]:
						l+=1
					while l<r and nums[r]==nums[r-1]:
						r-=1
					l += 1
					r -= 1
				elif nums[l]+nums[r] < -1*(nums[i]):
					l += 1
				else:
					r -= 1
		return res

nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
x = Solution()
print(x.threeSum(nums))
