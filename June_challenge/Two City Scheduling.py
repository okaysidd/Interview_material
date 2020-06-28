"""
Two City Scheduling
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].
Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

Example 1:
Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.
The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
"""
class Solution:
	"""
	Sort the list of lists by their differences, thus implying which ones
	will have maximum savings if picked. Pick the top half for A and bottom
	half for B (or vice versa, as applicable).
	"""
	def twoCitySchedCost(self, costs) -> int:
		costs.sort(key=lambda cost: cost[1]-cost[0])
		return sum([x[1] for x in costs[:len(costs)//2]]) + sum([x[0] for x in costs[len(costs)//2:]])

costs = [[10,20],[30,200],[400,50],[30,20]]
x = Solution()
print(x.twoCitySchedCost(costs))
