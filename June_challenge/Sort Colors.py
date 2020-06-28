"""
Sort Colors
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Note: You are not suppose to use the library's sort function for this problem.

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""
class Solution:
	"""
	Sorting will need O(nlogn) time or O(n) space.
	Dutch national flag technique skips both the problems.
	Keep low at 0 and high at the last of list, and a pointer
	named mid traverses through the list. If the mid encounters 1, just
	check next index, if it has 0, swap it with low position and increment
	both. "Low marks the first index after all 0s." If the index has 2,
	swap it with high index and decrease only high, as the high pointer
	marks the end of all 1s, but doesn't know what was swapped from its
	index, unlike for the low-mid swap.
	https://en.wikipedia.org/wiki/Dutch_national_flag_problem
	https://www.youtube.com/watch?v=BOt1DAvR0zI
	"""
	def sortColors(self, nums) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		low = mid = 0
		high = len(nums) - 1
		while mid < high:
			if nums[mid] == 1:
				mid += 1
			elif nums[mid] == 0:
				nums[mid], nums[low] = nums[low], nums[mid]
				mid += 1
				low += 1
			else:
				nums[mid], nums[high] = nums[high], nums[mid]
				high -= 1
		return nums # not necessary

nums = [2,0,2,1,1,0]
x = Solution()
print(x.sortColors(nums))
