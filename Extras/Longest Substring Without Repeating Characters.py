"""
Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution:
	"""
	left and right pointers to maintain unique substring between them, if right moves,
	add the character to set, if left moves, remove character from set.
	"""
	def lengthOfLongestSubstring(self, s: str) -> int:
		d = set()
		l = r = 0
		max_length = 0
		while l<=r and r<len(s):
			if s[r] not in d:
				d.add(s[r])
				r += 1
			else:
				d.remove(s[l])
				l += 1
			max_length = max(max_length, len(d))
		return max_length

s = "abcdscabc"
x = Solution()
print(x.lengthOfLongestSubstring(s))
