"""
Find Minimum in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
You may assume no duplicate exists in the array.

Example 1:
Input: [3,4,5,1,2] 
Output: 1

Example 2:
Input: [4,5,6,7,0,1,2]
Output: 0
"""
class Solution:
	"""
	In a rotated list, other than at the point of rotation, all other places,
	the increasing order will be maintained. At the point of rotation, the left
	will be larger than the right. We check for cases such as first number smaller
	than last, which means rotation did not happen.
	If the mid is less than the number at 0 index, it means that the point at which
	rotation happened is on the left. Otherwise on the right half.
	NOTE: IMPORTANT! Good use of binary search.
	THIS WORKS ONLY ON LISTS WITH DISTINCT NUMBERS.
	"""
	def findMin(self, nums):
		if len(nums) <= 2:
			return min(nums)
		if nums[0] < nums[-1]:
			return nums[0]
		# inflection point will have a non-increasing sequence
		l, r = 0, len(nums)-1
		while l<r:
			mid = l + (r - l) // 2
			print(l, mid, r)
			if nums[mid] > nums[mid+1]:
				return nums[mid+1]
			if nums[mid-1] > nums[mid]:
				return nums[mid]
			if nums[mid] > nums[0]:
				l = mid + 1
			else:
				r = mid - 1

nums = [4,5,6,7,1,2,3]
x = Solution()
print(x.findMin(nums))
