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

Note:
1 <= N <= 2000
0 <= dislikes.length <= 10000
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].
"""
import collections


class Solution:
	"""
	Graph question.
	Create a undirected graph using the dislikes couples list. Hence we save
	values for both directions.
	For a bipartite graph, if we prove that each neighbour of any particular
	node has different color than said node, we are sorted.
	We take this logic, and call a dfs method for all the nodes in the graph
	that we built, while maintaining all the nodes visited.
	If a node is not visited, assign it a color and opposite color to all its
	neighbors. If the node was already visited, check it for conflicts.
	# NOTE: IMPORTANT!
	"""
	def possibleBipartition(self, N: int, dislikes):
		graph = collections.defaultdict(list)

		for i in dislikes:
			graph[i[0]].append(i[1]) # create undirected graphs
			graph[i[1]].append(i[0]) # therefore flow can be both ways

		visited = {} # dict to maintain all nodes visited

		def dfs(node, color):
			# check the node for color conflicts if already visited
			if node in visited:
				return visited[node] == color

			# record color if not visited
			visited[node] = color

			return all([dfs(neighbor, 1-color) for neighbor in graph[node]])

		res = all([dfs(node, 1) for node in graph if node not in visited])
		"""
		since we are alloting a color manually (1 here), we'll only send those
		nodes to the dfs function that have not already been visited. Because
		if a node has been set to 0, and we call dfs on it with color 1, it'll
		create a conflict, resulting in False result incorrectly.
		"""
		return res

N = 5
dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
x = Solution()
print(x.possibleBipartition(N, dislikes))
