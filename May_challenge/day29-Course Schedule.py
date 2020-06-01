"""
Course Schedule
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
			 To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
			 To take course 1 you should have finished course 0, and to take course 0 you should
			 also have finished course 1. So it is impossible.
"""
class Solution:
	"""
	Classic graph question to detect cycle in directed graph.
	Below solution is for Topological sorting, using Kahn's algorithm.
	If cycle exists, the topologically sorted solution cannot be found.
	This can also be done by graph dfs.
	# NOTE: IMPORTANT!
	"""
	def canFinish(self, numCourses: int, prerequisites) -> bool:
		# build ajdacency list (for graph representation)- flow of courses to be taken: b->a
		graph = [[] for _ in range(numCourses)]
		for a, b in prerequisites:
			graph[b].append(a)
		
		# build degrees list for all nodes- flow of courses to be taken: b->a, thus we count incoming on a
		degree = [0]*numCourses
		for a, b in prerequisites:
			degree[a] += 1
			
		# queue of all edges with no incoming edge- mandatory in a topological sort-able graph
		queue = []
		for node, deg in enumerate(degree):
			if deg == 0:
				queue.append(node)
				
		# visited vertices count
		count = 0
		# topological order list
		top = []
		
		while queue:
			head = queue.pop(0)
			count += 1
			top.append(head)
			
			for node in graph[head]:
				degree[node] -= 1
				if degree[node] == 0:
					queue.append(node)
					
		return count == numCourses

numCourses = 2
prerequisites = [[1,0],[0,1]]
x = Solution()
print(x.canFinish(numCourses, prerequisites))
