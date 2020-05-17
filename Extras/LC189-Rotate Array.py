"""
189. Rotate Array
Given an array, rotate the array to the right by k steps, where k is non-negative.
Follow up:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Constraints:
1 <= nums.length <= 2 * 10^4
It's guaranteed that nums[i] fits in a 32 bit-signed integer.
k >= 0
"""
class Solution:
	"""
	While straight forward, the problem lies with Python lists that are mutable
	and do not create a copy of an object while assignment, but create new
	reference to the same object. So nums actually does not change on the assignment,
	but creating a shallow copy using nums[:] does the trick.
	https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/
	"""
	def rotate(self, nums, k):
		"""
		Do not return anything, modify nums in-place instead.
		"""
		k = k % len(nums)
		nums[:] = nums[-1*k:] + nums[:-k]
		return nums

nums = [1,2,3,4,5,6,7,8]
k = 3
x = Solution()
print(x.rotate(nums, k))
