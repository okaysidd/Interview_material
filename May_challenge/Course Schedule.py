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

# to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
class Solution2:
	"""
	Using DFS. If a backward edge is encountered, return False.
	Makes some improvement over basic DFS, but using a visited list, with all 0s.
	If the node is currently getting visited, mark it -1, so if in the
	DFS recursion, it is reached again, it will denote a backward edge.
	After all processing, mark the visited as 1, to say that if we start
	DFS from this node, no backward edge exists.
	"""
	def canFinish(self, numCourses: int, prerequisites) -> bool:
		adj = {x:[] for x in range(numCourses)}
		for i in prerequisites:
			adj[i[1]].append(i[0])
		visit = [0 for _ in range(numCourses)]
		def helper(node):
			if visit[node] == -1:
				return False
			if visit[node] == 1:
				return True
			visit[node] = -1
			for neighbor in adj[node]:
				if helper(neighbor) == False:
					return False
			visit[node] = 1
			return True
		for node in adj:
			if helper(node) == False:
				return False
		return True

class Solution3:
	"""
	Using DFS. If a backward edge is encountered, return False.
	Maintains a current_stack to record all nodes in the running
	inner recursion stack. If one of those nodes is re-visited, it
	means a backward edge exists.
	"""
	def canFinish(self, numCourses: int, prerequisites) -> bool:
		adj = {x:[] for x in range(numCourses)}
		for i in prerequisites:
			adj[i[1]].append(i[0])
		BACK_EDGE = False
		def dfs_visit(node, parent=None, current_stack=None):
			if current_stack and node in current_stack:
				nonlocal BACK_EDGE
				BACK_EDGE = True
			if current_stack == None: current_stack = set()
			if parent == None: parent = {}
			current_stack.add(node)
			for neighbor in adj[node]:
				if neighbor not in parent:
					parent[neighbor] = node
					dfs_visit(neighbor, parent, current_stack)
			current_stack = set()
		for node in adj:
			dfs_visit(node)
			if BACK_EDGE == True:
				return False
		return True

numCourses = 3
prerequisites = [[1,0],[0,2]]
x = Solution()
print(x.canFinish(numCourses, prerequisites))
x = Solution2()
print(x.canFinish(numCourses, prerequisites))
x = Solution3()
print(x.canFinish(numCourses, prerequisites))
