"""
Group Anagrams
Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
All inputs will be in lowercase.
The order of your output does not matter.
"""
class Solution:
	def groupAnagrams(self, strs):
		d = {}
		for st in strs:
			st1 = ''.join(sorted(st))
			if st1 in d.keys():
				d[st1].append(st)
			else:
				d[st1] = [st]
		return list(d.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat", "banana", "baaann"]
a = Solution()
print(a.groupAnagrams(strs))
