"""
Contiguous Array
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""
class Solution:
	def findMaxLength(self, nums):
		d = {0:-1}
		counter = 0
		max_ = 0
		for i in range(len(nums)):
			if nums[i] == 0:
				counter += -1
			else:
				counter += 1
			if counter in d.keys():
				max_ = max(max_, i-d[counter])
			else:
				d[counter] = i
		return max_


class Solution2:
	"""
	Solved in may challenge by self.
	If we consider 0s as -1 and 1s as +1, we can plot the input
	as a graph with peaks and valleys.
	Basic premise is that if there exist two valley with same depth
	or two peaks with same height, number of 1s and 0s between them
	will be the same.
	Target is to find farthest such incidents. So we save all occurences
	of peaks and valleys in a dict, with the index that they occured on.
	Then we take of max difference of the indices that we stored for a
	particular peak/valley point.
	"""
	def findMaxLength(self, nums: List[int]) -> int:
		d = {0:[0]}
		dp_prev, dp_current = 0, 0
		for i in range(len(nums)):
			temp = -1 if not nums[i] else nums[i]
			dp_current = dp_prev + temp
			if dp_current in d.keys():
				d[dp_current].append(i+1)
			else:
				d[dp_current] = [i+1]
			dp_prev = dp_current
		max_ = 0
		for key, index in d.items():
			max_ = max(max_, abs(index[0]-index[-1]))
		return max_

a = Solution()
nums = [0,1,0,1,0,1,1,0]
print(a.findMaxLength(nums))