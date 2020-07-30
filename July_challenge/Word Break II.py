"""
Word Break II
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.
Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""
class Solution:
	"""
	No idea how this works.
	"""
	def wordBreak(self, s, wordDict):
		return self.help(s, wordDict, {})

	def help(self, s, wordDict, memo):
		if s in memo:
			return memo[s]
		res = []
		if len(s) == 0:
			res += ['']
			return res
		substrings = []
		for word in wordDict:
			if s.startswith(word):
				sub = s[len(word):]
				substrings = self.help(sub, wordDict, memo)
				for subst in substrings:
					res.append(word + ' ' + subst)
		memo[s] = [x.strip() for x in res]
		return memo[s]

s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple", "some", "orange"]
x = Solution()
x.wordBreak(s, wordDict)
