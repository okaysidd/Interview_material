"""
Uses of DFS:
- Topological sorting
- Finding cycles in graph (if a backward edge exists)
- Classifying edges of graph
	For Directed graph:
	-- Tree edges, Non-tree (forward, backward, cross edges)
	For Un-directed graph:
	-- Tree edges, backward edge
"""
class DepthFirstSearch:
	"""
	Finds DFS route as well as whether the graph has a cycle/has a backward
	edge/can be topologically sorted.
	Pick a node and one of it neighbor and repeat. Go as deep as possible
	and then backtrack and go another route, like solving a maze. The stack
	is implicitly handled by the recursion stack.
	"""
	def dfs(self, graph):
		"""
		Used to call all the nodes once so that no node, even if unconnected,
		is left behind. Starting-node-choser.
		"""
		parent_outer = {}
		for start_node in graph:
			if start_node not in parent_outer:
				parent_outer[start_node] = self.dfs_visit(graph, start_node)
		return parent_outer
	def dfs_visit(self, graph, start_node, parent=None, current_stack=None):
		"""
		Actually the main function that takes a graph and a starting node
		and returns all the nodes reachable from that node using depth first
		search.
		"""
		if parent == None:
			parent = {start_node:None}
		for node in graph[start_node]:
			if current_stack and node in current_stack:
				print(f'back: {node, start_node}')
			if current_stack == None:
				current_stack = {node}
			else:
				current_stack.add(node)
			if node not in parent:
				parent[node] = start_node
				self.dfs_visit(graph, node, parent, current_stack)
			current_stack = None
		return parent

class DepthFirstSearch2:
	"""
	Better code with single function.
	"""
	def dfs(self, graph):
		def dfs_visit(node, parent=None, current_stack=None):
			if parent == None:
				parent = {node:None}
			for neighbor in graph[node]:
				if current_stack and neighbor in current_stack:
					nonlocal BACK_EDGE
					BACK_EDGE = True
				if current_stack == None: current_stack = {neighbor}
				else: current_stack.add(neighbor)
				if neighbor not in parent:
					parent[neighbor] = node
					dfs_visit(neighbor, parent, current_stack)
				current_stack = None
			return parent
		parent_outer = {}
		BACK_EDGE = False
		for node in graph:
			parent_outer[node] = dfs_visit(node)
		return parent_outer, BACK_EDGE

# TODO: Change to print actual route and the parent dict (if possible)

from Input_for_graphs import GraphInput
a = GraphInput()
graph_C = a.get_directed_cyclic_adj()
graph_AC = a.get_directed_acyclic_adj()

x = DepthFirstSearch()
print(x.dfs(graph_C))
print()
print(x.dfs(graph_AC))
# x = DepthFirstSearch2()
# print(x.dfs(edges1))
# print(x.dfs(edges2))
