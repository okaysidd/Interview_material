"""
Permutation in String
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""
class Solution:
    """
    Same as day17 in here.
    Have to maintain a counter of char frequencies, can do using a
    26 len list or a dict.
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dp1 = [0]*26
        dp2 = [0]*26
        for i in s1:
            dp1[ord(i)-97] += 1
        for i in range(len(s2)):
            dp2[ord(s2[i])-97] += 1
            if dp1 == dp2:
                return True, i
            if i >= len(s1)-1:
                dp2[ord(s2[i-(len(s1)-1)])-97] -= 1
        return False


class Solution2:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = {}
        d2 = {}
        for i in s1:
            if i in d1.keys():
                d1[i] += 1
            else:
                d1[i] = 1
        for i in range(len(s2)):
            if sum(d2.values()) >= len(s1):
                d2[s2[i-len(s1)]] -= 1
                if d2[s2[i-len(s1)]] == 0:
                    d2.pop(s2[i-len(s1)])
            if s2[i] in d2.keys():
                d2[s2[i]] += 1
            else:
                d2[s2[i]] = 1
            if d1 == d2:
                return True
        return False


s1 = "ab"
s2 = "eidbaooo"
x = Solution()
print(x.checkInclusion(s1, s2))
