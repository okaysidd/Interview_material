"""
Edit Distance
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
You have the following 3 operations permitted on a word:
Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""
class Solution:
	"""
	Very important and classic dynamic programming problem. The dp
	is arranged here with starting numbers of characters alterations
	required if the other word was null. For example, for 'abc' and 'ad',
	the original dp matrix is arranged as follows.
	
	[0, 1, 2, 3] <-- number of alterations (deletions or additions) required if other word was ''
	[1, 0, 0, 0]
	[2, 0, 0, 0]
	^
	|
	number of alterations
	(deletions or additions)
	required if other word was ''

	Then we fill every other cell like normal dp problems, if the characters
	at the current cell in both words are same, no alterations will be
	required, hence pick the diagonal up-left number and store it at
	current cell. Otherwise pick the minimum of these three- left, up and
	diagonal up-left, and add 1 to it for the current cell alteration.
	dp[-1][-1] gives the answer.
	A solution which does not hold the complete matrix in the memory all
	the time is also possible. Will explore that.
	# NOTE: IMPORTANT!!
	"""
	def minDistance(self, word1: str, word2: str) -> int:
		dp = [[0 for i in word1 + ' '] for j in word2 + ' ']
		for i in range(len(dp)):
			dp[i][0] = i
		for i in range(len(dp[0])):
			dp[0][i] = i
		for i in range(len(word2)): # for looping over rows
			for j in range(len(word1)): # for looping over elements of each row
				if word2[i] == word1[j]:
					dp[i+1][j+1] = dp[i][j]
				else:
					dp[i+1][j+1] = 1 + min(dp[i][j+1], dp[i+1][j], dp[i][j])
		return dp[-1][-1]

word1 = 'siddhartha'
word2 = 'siddhant'
x = Solution()
print(x.minDistance(word1, word2))
