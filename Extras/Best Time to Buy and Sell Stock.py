"""
121. Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
			 Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
class Solution:
	"""
	OK, simply put, have to find max difference between two numbers in the
	list such that buy-number occurs before the sell-number.
	Using brute force, it is clear that for every instance in the outer
	loop (i), the inner loop will only run from i+1 to the end, and not
	the complete arary (since buy before sell policy).
	So instead of running two loops, we update min price to buy at, at every
	step, while updating maxprofit (earlier or current i - (the updated) minprice).
	NOT-NEEDED~~~Conversely if we maintain max price like we are maintaining min price,
	that will result in the max price, irrespective of its position.
	So instead we subtract at each step from the minprice till that point
	to make sure we pick sell after buy.~~~NOT-NEEDED
	"""
	def maxProfit(self, prices):
		minprice = 99999
		maxprofit = 0
		for i in prices:
			minprice = min(minprice, i)
			maxprofit = max(maxprofit, i-minprice)
		return maxprofit

prices = [7,1,5,3,6,4]
a = Solution()
print(a.maxProfit(prices))
