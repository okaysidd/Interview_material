"""
Online Stock Span
Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.
The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.
For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

Example 1:
Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
Output: [null,1,1,1,2,1,4,6]
Explanation: 
First, S = StockSpanner() is initialized.  Then:
S.next(100) is called and returns 1,
S.next(80) is called and returns 1,
S.next(60) is called and returns 1,
S.next(70) is called and returns 2,
S.next(60) is called and returns 1,
S.next(75) is called and returns 4,
S.next(85) is called and returns 6.

Note that (for example) S.next(75) returned 4, because the last 4 prices
(including today's price of 75) were less than or equal to today's price.
"""
class StockSpanner:
	"""
	Whenever a larger number arrives, using stack to maintain that
	on the top of stack and with it the number of entries that were
	lower than can be skipped if the top larger number is even smaller
	than a new price. However if a smaller price arrives than the
	top of the stack, then just add it to stack with the partner entry 1.
	# NOTE: IMPORTANT!
	"""
	def __init__(self):
		self.stack = []

	def next(self, price: int) -> int:
		weight = 1
		while self.stack and self.stack[-1][0] <= price:
			weight += self.stack.pop()[1]
		self.stack.append((price, weight))
		return weight

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

command = ["StockSpanner","next","next","next","next","next","next","next"]
arg = [[],[1],[1],[1],[2],[1],[1],[1]]
for i in range(len(command)):
	if command[i] == "next":
		S.next(arg[i][0])
	else:
		S = StockSpanner()
