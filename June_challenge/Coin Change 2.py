"""
Coin Change 2
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Example 1:
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10] 
Output: 1
"""
class Solution:
	"""
	Recursive dp solution using memoization. Slow (but much faster than without memo).
	"""
	def change(self, amount, coins, memo=None):
		if memo == None:
			memo = {}
		if (amount, tuple(coins)) in memo:
			return memo[(amount, tuple(coins))]
		if amount == 0:
			return 1
		if amount < 0 or len(coins) <= 0:
			return 0
		memo[(amount, tuple(coins))] = self.change(amount-coins[0], coins, memo) \
			+ self.change(amount, coins[1:], memo)
		return memo[(amount, tuple(coins))]

class Solution2:
	"""
	Bottom-up dp solution dp table. For each coin, calculate the combinations,
	in a dp array that represents the amount. We do it for each coin (thus coin
	on outer loop), because it is a combination and not permutation.
	"""
	def change(self, amount, coins, memo=None):
		dp = [0] * (amount + 1)
		dp[0] = 1
		# ^ important- signifies that if no amount is to be made, it can be done in 1 way, taking no coin
		for coin in coins:
			for amount_index in range(1, len(dp)):
				if amount_index >= coin:
					dp[amount_index] += dp[amount_index-coin]
					# ^ if going with same coin, ways to create numbers in multiple of that will remain same
		return dp[-1]

amount = 200
coins = [1, 2, 5]
x = Solution2()
print(x.change(amount, coins))
