"""
Bitwise AND of Numbers Range
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.


Input: [5,7]
Output: 4

Example 2:
Input: [0,1]
Output: 0
"""
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        count = 0
        while m!=n:
            count += 1
            m=m>>1
            n=n>>1
        return m<<count

a = Solution()
m = 5
n = 7
print(a.rangeBitwiseAnd(m, n))
