"""
Increasing Triplet Subsequence
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:
Input: [1,2,3,4,5]
Output: true

Example 2:
Input: [5,4,3,2,1]
Output: false
"""
class Solution:
	"""
	Great solution to take insanely large left and mid values, then start comparing
	each value in the list by mid and left. If the number is lesser than left, assign
	it to left. If the number comes between left and mid, assign it to mid. If the number
	is larger than mid, it means we have found all three values; this will happen only
	if we have take truly insanely large values.
	"""
	def increasingTriplet(self, nums):
		left, mid = 99999999999999, 99999999999999
		for n in nums:
			if n > mid:
				return True
			if n < left:
				left = n
			elif n < mid and n > left:
				mid = n
		return False

nums = [1,4,4,4,60000]
x = Solution()
print(x.increasingTriplet(nums))
