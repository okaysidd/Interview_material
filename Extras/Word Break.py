"""
Word Break
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
class Solution:
    """
    Logic here is to check if a part of the string is in the dictionary,
    and "if it is", recursively call the same function on rest of the part.
    # NOTE: IMPORTANT!!
    """
    def wordBreak(self, s: str, wordDict):
        if len(s) == 0 or s in wordDict: return True
        if len(wordDict) == 0: return False

        memo = {}
        
        def some(s, d):
            nonlocal memo
            if s in memo:
                return memo[s]
            if s in d:
                memo[s] = True
                return True
            for i in range(1, len(s)):
                memo[s[i:]] = some(s[i:], d)
                if s[:i] in d and memo[s[i:]]:
                    memo[s] = True
                    return True
            return False

        return some(s, set(wordDict))

    def wordBreak2(self, s: str, wordDict): # non-memoized for readability
        if len(s) == 0 or s in wordDict: return True
        if len(wordDict) == 0: return False
        if s in wordDict:
            return True
        for i in range(1, len(s)):
            if s[:i] in wordDict and self.wordBreak2(s[i:], wordDict):
                return True
        return False

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
x = Solution()
print(x.wordBreak(s, wordDict))
