"""
91. Decode Ways
Medium
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.
Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""
class Solution:
    """
    https://www.youtube.com/watch?v=qli-JCrSwuk
    12345 -> can be decode either as 'a' + decode('2345') or 'l' + decode('345').
    This is the intuition. When '' is reached, return 1.
    Special case is when s (='330') starts with first two digits greater than 26, in which
    case only the 'c' + decode('30') case stands, since '33' has no translation.
    """
    def numDecodings(self, s: str, memo=None) -> int:
        if memo == None:
            memo = {}
        if s in memo.keys():
            return memo[s]
        if s == '':
            return 1
        if int(s[0]) == 0:
            return 0
        if len(s) == 1:
            return 1
        if int(s[:2]) <= 26:
            memo[s] = self.numDecodings(s[1:], memo) + self.numDecodings(s[2:], memo)
        else:
            memo[s] = self.numDecodings(s[1:], memo)
        return memo[s]

s = '330'
a = Solution()
print(a.numDecodings(s))
