"""
Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
"""

class Solution1:
    def singleNumber(self, nums):
        d = {}
        for i in nums:
            try:
                d[i] += 1
            except:
                d[i] = 1
        return [f for f in d.keys() if d[f] == 1][0]


import operator, functools

class Solution2:
    """
    Uses XOR to figure which number occurs only once
    """
    def singleNumber(self, nums):
        return functools.reduce(operator.ixor, nums)


a = Solution1()
items = [4,1,2,1,2]
result = a.singleNumber(items)
print(result)
