"""
Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 
Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        a = 0
        while n != 1 and n not in seen:
            a = 0
            seen.add(n)
            while n > 0:
                a += (n % 10) ** 2
                n = n // 10
            n = a
        if n == 1:
            return True
        return False

a = Solution()
print(a.isHappy(19))

# uses trickery to stop after 10 iterations, assuming that would be enough
class Solution:
    def isHappy(self, n: int, n_prev=0) -> bool:
        if n == 1:
            return True
        if n_prev > 10:
            return False
        n_prev += 1
        a = 0
        while n > 0:
            a += (n % 10) ** 2
            n = n //10
        return self.isHappy(a, n_prev)