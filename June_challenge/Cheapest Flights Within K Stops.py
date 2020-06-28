"""
Cheapest Flights Within K Stops
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.
Now given all the cities and flights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The cheapest price from city 0 to city 2 with at most 1 stop costs 200.

Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The cheapest price from city 0 to city 2 with at most 0 stop costs 500.
"""
class Solution:
	"""
	BFS with modification.
	Instead of checking the visited (or levels or parents) nodes to skip nodes
	that are already visited, stopping condition is the stops reaching the number
	of maximum stops required.
	# NOTE: IMPORTANT!
	"""
	def findCheapestPrice(self, n, flights, src, dst, K):
		adj = {x:[] for x in range(n)}
		for i in flights:
			adj[i[0]].append((i[1], i[2]))
		frontier = [(src, 0)]
		result = 9999999
		stops = 0
		while frontier:
			next_frontier = []
			for node, current_cost in frontier:
				if node == dst and stops <= K+1: # reached destination in K or fewer stops
					result = min(result, current_cost)
				elif current_cost < result and stops <= K+1:
					for neighbor, new_cost in adj[node]:
						next_frontier.append((neighbor, current_cost+new_cost))
			frontier = next_frontier
			stops += 1
		return -1 if result == 9999999 else result

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
K = 1
x = Solution()
print(x.findCheapestPrice(n, flights, src, dst, K))
