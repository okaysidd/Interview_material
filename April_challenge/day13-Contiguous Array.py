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

a = Solution()
nums = [0,1,0,1,0,1,1,0]
print(a.findMaxLength(nums))