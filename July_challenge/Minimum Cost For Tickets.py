"""
Minimum Cost For Tickets
In a country popular for train travel, you have planned some train travelling one year in advance.  The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.
Train tickets are sold in 3 different ways:
a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.

Example 1:
Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total you spent $11 and covered all the days of your travel.

Example 2:
Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: 
For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total you spent $17 and covered all the days of your travel.

Note:
1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000
"""
class Solution:
	"""
	Top down approach.
	Maintain dp table, at each day, if you buy 1 day ticket, get value for yesterday
	as well, if you buy 7 days ticket, get 7-day prior value, similarly for 30 days.
	Get their minimum.
	Of course, if the day is not a travelling day, carry forward previous day's result,
	as we have no need to buy ticket today.
	Last index we'll get the answer.
	"""
	def mincostTickets(self, days, costs):
		dp = [0]*366
		for day in range(1, len(dp)):
			if day not in days:
				dp[day] = dp[day-1]
			else:
				dp[day] = min(
					dp[day-1] + costs[0],
					dp[max(0, day-7)] + costs[1],
					dp[max(0, day-30)] + costs[2],
				)
		return dp[-1]

class Solution2:
	"""
	Bottom up approach.
	Start from 0 and check till 365 days (the constraints), if day is outside [0, 365) range,
	return 0.
	Now for days that we are not travelling, we should not buy tickets for those days, so in
	such cases, return the answer as whatever is the answer for next day.
	If we do have to travel for that day, get minimum of 3 conditions, if we buy 1 day ticket
	(so add 1 day cost and next days answer), if we buy 7 days ticket (so add 7 days cost and 
	answer for 7 days after current day), and so on.
	Memo to hold if some days might have been pre-calculated.
	# NOTE: IMPORTANT! Good question.
	"""
	def mincostTickets(self, days, costs):
		memo = {}
		days = [x-1 for x in days] # to make it 0 indexed
			
		def some(day):
			if day in memo:
				return memo[day]
			
			nonlocal days, costs
			
			if day<0 or day>=365:
				return 0
			
			if day not in days:
				return some(day+1)
			
			buy1 = some(day+1) + costs[0]
			buy7 = some(day+7) + costs[1]
			buy30 = some(day+30) + costs[2]
			
			memo[day] = min(buy1, buy7, buy30)
			return memo[day]
		
		return some(0)

days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]
x = Solution()
print(x.mincostTickets(days, costs))
