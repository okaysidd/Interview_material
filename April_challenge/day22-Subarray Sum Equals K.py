"""
Subarray Sum Equals K
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""
class Solution:
	"""
	Sort of Google's video question, but changed to add sum upto the
	current element in a dict (with frequencies) and subtract the current
	element to check if the rest of the sum lies anywhere.
	sum - k = current_element
	"""
    def subarraySum(self, nums, k):
        s = 0
        a_sum = {0:1}
        res = 0
        for i in range(len(nums)):
            s += nums[i]
            if s-k in a_sum.keys():
                res += a_sum[s-k]
            if s in a_sum.keys():
                a_sum[s] += 1
            else:
                a_sum[s] = 1
        return res

nums = [1,1,1]
k = 2
a = Solution()
print(a.subarraySum(nums, k))
