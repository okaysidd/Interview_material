"""
Possible Bipartition
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.
Each person may dislike some other people, and they should not go into the same group. 
Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.
Return true if and only if it is possible to split everyone into two groups in this way.

Example 1:
Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]

Example 2:
Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false

Example 3:
Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
"""
import collections

class Solution:
	"""
	Classic graph Bipartite problem.
	Uses groups/colors to separate the nodes in two different
	groups. DFS is used. Starting from each node, assign it a color
	and assign the opposite color to all its derivatives. Then
	the opposite color to all their derivatives. If at any point
	a contradiction arises, the bipartite is not possible.
	https://en.wikipedia.org/wiki/Bipartite_graph
	"""
	def possibleBipartition(self, N: int, dislikes) -> bool:
		graph = collections.defaultdict(list)
		for i in dislikes:
			graph[i[0]].append(i[1])
			graph[i[1]].append(i[0])
		visited = {} # dict to maintain all nodes visited

		def dfs(node, color):
			# check the node for color conflicts if already visited
			if node in visited:
				return visited[node] == color
			# record color if not visited
			visited[node] = color
			return all([dfs(neighbor, 1-color) for neighbor in graph[node]])

		res = all([dfs(node, 1) for node in graph])
		return res

N = 5
dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
x = Solution()
print(x.possibleBipartition(N, dislikes))
