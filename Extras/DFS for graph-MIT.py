"""
Uses of DFS:
- Topological sorting
- Finding cycles in graph
- Classifying edges of graph
	For Directed graph:
	-- Tree edges, Non-tree (forward, backward, cross edges)
	For Un-directed graph:
	-- Tree edges, backward edge
"""
class DepthFirstSearch:
	"""
	Pick a node and one of it neighbor and repeat. Go as deep as possible
	and then backtrack and go another route, like solving a maze. The stack
	is implicitly handled by the recursion stack.
	"""
	def dfs(self, graph, parent_outer=None):
		"""
		Used to call all the nodes once so that no node, even if unconnected,
		is left behind. Starting-node-choser.
		"""
		if parent_outer == None:
			parent_outer = {}
		for start_node in graph:
			if start_node not in parent_outer:
				parent_outer[start_node] = self.dfs_visit(graph, start_node)
		return parent_outer
	def dfs_visit(self, graph, start_node, parent=None):
		"""
		Actually the main function that takes a graph and a starting node
		and returns all the nodes reachable from that node using depth first
		search.
		"""
		if parent == None:
			parent = {start_node:None}
		for node in graph[start_node]:
			if node not in parent:
				parent[start_node] = node
				return self.dfs_visit(graph, node, parent)
		return parent

graph = {
	's': ['a', 'b'],
	'a': ['c'],
	'b': ['c', 'd'],
	'c': ['d', 'e', 'a'],
	'd': ['e'],
	'e': ['c', 'd'],
	'f': []
}
x = DepthFirstSearch()
print(x.dfs(graph))
