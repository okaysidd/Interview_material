"""
Reconstruct Itinerary

Solution
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
			 But it is larger in lexical order.
"""
class Solution:
	def findItinerary(self, tickets):
		adj = {}
		for x, y in tickets[::-1]:
			if x in adj:
				adj[x].append(y)
			else:
				adj[x] = [y]
		result = []
		def dfs(node):
			while node in adj and len(adj[node]) != 0:
				dfs(adj[node].pop())
			result.append(node)
			pass
		
		dfs('JFK')
		return result[::-1]

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
x = Solution()
print(x.findItinerary(tickets))
