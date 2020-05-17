"""
Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""
class Solution:
	"""
	Using modified Binary search, first find the original starting
	point of the now-rotated array. Then splitting the array there,
	figure which half will the target be. Do Binary search again in
	there. O(log n) twice.
	"""
    def search(self, nums, target):
        if len(nums) < 1:
            return -1
        if target == nums[0]:
            return 0
        L = 0
        R = len(nums) - 1
        while L <= R:
            mid = (R+L)//2
            if nums[mid] < nums[R]:
                R = mid
            else:
                L = mid + 1
        loc = R
        if target == nums[loc]:
            return loc
        if target > nums[-1]:
            L = 0
            R = loc
        else:
            L = loc+1
            R = len(nums)
        while L < R:
            mid = (R + L) // 2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                L = mid + 1
            else:
                R = mid
        return -1

nums = [4,5,6,7,0,1,2]
target = 0

a = Solution()
print(a.search(nums, target))
