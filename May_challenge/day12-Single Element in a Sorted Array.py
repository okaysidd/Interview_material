"""
Single Element in a Sorted Array
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
Note: Your solution should run in O(log n) time and O(1) space.
"""
class Solution:
	"""
	Can be solved using ^ (xor) operator but that'll take O(n) time,
	while here since the list is sorted, we can use that property to
	use Binary search.
	Trick here is to realise that till the single element occurence,
	the first occurence of the pair will be at even positions and the
	second at the odd positions. That will change however when the single
	number occurs, post which the first occurence of the pairs will be at
	the odd positions and second at even positions.
	"""
	def singleNonDuplicate(self, nums) -> int:
		if len(nums) == 1:
			return nums[0]
		l = 0
		r = len(nums)-1
		# print(l, r)
		while l<r and r < len(nums) and r-l > 1:
			mid = (l+r)//2
			# print(mid)
			if nums[mid-1] != nums[mid] and nums[mid+1] != nums[mid]:
				return nums[mid]
			if mid % 2 == 0:
				if nums[mid+1] == nums[mid]:
					l = mid
				else:
					r = mid
			else:
				if nums[mid-1] == nums[mid]:
					l = mid
				else:
					r = mid
		if nums[mid] == nums[l]:
			return nums[r]
		return nums[l]

nums = [1,1,2,2,3,3,4,4,8]
x = Solution()
print(x.singleNonDuplicate(nums))
