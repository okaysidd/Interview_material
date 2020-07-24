"""
Stone Game IV
Alice and Bob take turns playing a game, with Alice starting first.
Initially, there are n stones in a pile.  On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.
Also, if a player cannot make a move, he/she loses the game.
Given a positive integer n. Return True if and only if Alice wins the game otherwise return False, assuming both players play optimally.

Example 1:
Input: n = 1
Output: true
Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.

Example 2:
Input: n = 2
Output: false
Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).

Example 3:
Input: n = 4
Output: true
Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).

Example 4:
Input: n = 7
Output: false
Explanation: Alice can't win the game if Bob plays optimally.
If Alice starts removing 4 stones, Bob will remove 1 stone then Alice should remove only 1 stone and finally Bob removes the last one (7 -> 3 -> 2 -> 1 -> 0). 
If Alice starts removing 1 stone, Bob will remove 4 stones then Alice only can remove 1 stone and finally Bob removes the last one (7 -> 6 -> 2 -> 1 -> 0).

Example 5:
Input: n = 17
Output: false
Explanation: Alice can't win the game if Bob plays optimally.
"""
class Solution:
	"""
	https://leetcode.com/problems/stone-game-iv/discuss/730942/Standard-DP-question-Explained-BEST-ALL-you-need-to-know
	For each state i:
	j = find all the perfect squares less than i.
	for each j:
		Assume that the perfectsquare j is taken by alice.
		Then the game continues as` dp[i-j*j]` for bob as start player.
		Since we calculated all answers for such states with alice as start player,its the same even if bob becomes the start player because both play optimally.
		If bob could wins ,alice loses i.e ` dp[i-j*j]` = True
		else if bob loses alice wins    i.e ` dp[i-j*j]`  = False
		So,we choose the case where alice wins with alice as start player(In essence we find if atleast one j returns True for dp[i]). or dp[i] |= ! dp[i-j*j]
	"""
	def winnerSquareGame(self, n: int) -> bool:
		dp = [False]*(n+1) # this is actually faster than list comprehension (around 10 times), use where possible
		for i in range(1, n+1):
			j = 1
			while j*j <= i:
				dp[i] |= not dp[i - j*j]
				j += 1
		return dp[-1]

n = 17
x = Solution()
print(x.winnerSquareGame(n))
