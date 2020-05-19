"""
Find All Anagrams in a String
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output:
[0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"
Output:
[0, 1, 2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
class Solution:
	"""
	Same as day18 in here.
	Just have to get all the anagrams.
	Maintain a 26 char list for char frequencies.
	"""
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dp1 = [0]*26
        dp2 = [0]*26
        for i in p:
            dp1[ord(i)-97] += 1
        res = []
        for i in range(len(s)):
            dp2[ord(s[i])-97] += 1
            if dp1 == dp2:
                res.append(i-len(p)+1)
            if i >= len(p)-1:
                dp2[ord(s[i-(len(p)-1)])-97] -= 1
        return res

s = "cbaebabacd"
p = "abc"
x = Solution()
print(x.findAnagrams(s, p))
