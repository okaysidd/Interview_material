"""
Search for a Range
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
class Solution:
	"""
	Good question. Apart from linear scan O(n), we can use Binary search O(lg(n)),
	since the list is sorted.
	Thing to note is that finding the first occurance of target with binary search
	is straight forward, since the target occurences will be all next to each other,
	because list is sorted.
	"""
	def searchRange(self, nums, target):
		l, r = 0, len(nums)-1
		res = [-1, -1]
		while l <= r:
			mid = l + ((r-l) // 2)
			if target < nums[mid]:
				r = mid - 1
			elif target > nums[mid]:
				l = mid + 1
			else:
				res[0] = mid
				while mid>0 and nums[mid] == target:
					if nums[mid-1] == target:
						res[0] = mid-1
					mid -= 1
				break
		if res[0] == -1: return res
		l, r = 0, len(nums)-1
		while l <= r:
			mid = l + ((r-l) // 2)
			if target < nums[mid]:
				r = mid - 1
			elif target > nums[mid]:
				l = mid + 1
			else:
				res[1] = mid
				while mid<len(nums)-1 and nums[mid] == target:
					if nums[mid+1] == target:
						res[1] = mid+1
					mid += 1
				break
		return res

nums = [5,7,7,8,8,10]
target = 6
x = Solution()
print(x.searchRange(nums, target))
