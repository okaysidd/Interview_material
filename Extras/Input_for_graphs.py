"""
Input for Graph questions.
"""
class GraphInput:
	def __init__(self):
		self.NUMBER_OF_NODES = 6

	def get_directed_cyclic_edges(self):
		# DIRECTED - CYCLIC - EDGES
		edgesDCE = [(1,2), (1,3), (2,4), (3,4), (3,5), (4,5), (5,6), (6,4)]
		return edgesDCE

	def get_directed_cyclic_adj(self):
		edges = self.get_directed_cyclic_edges()
		adj = {x:[] for x in range(1, self.NUMBER_OF_NODES+1)}
		for u, v in edges:
			adj[u].append(v)
		return adj

	def get_directed_acyclic_edges(self):
		# DIRECTED - ACYCLIC - EDGES
		edgesDAE = [(1,2), (1,3), (2,4), (3,4), (3,5), (5,4), (5,6), (6,4)]
		return edgesDAE

	def get_directed_acyclic_adj(self):
		edges = self.get_directed_acyclic_edges()
		adj = {x:[] for x in range(1, self.NUMBER_OF_NODES+1)}
		for u, v in edges:
			adj[u].append(v)
		return adj

	def get_undirected_cyclic_edges(self):
		# UNDIRECTED - CYCLIC - EDGES
		edgesUCE = [(1,2), (2,1), (2,4), (4,2), (3,4), (4,3), (3,5), (5,3), \
			(5,6), (6,5), (1,3), (3,1), (4,5), (5,4), (4,6), (6,4)]
		return edgesUCE

	def get_undirected_cyclic_adj(self):
		edges = self.get_undirected_cyclic_edges()
		adj = {x:[] for x in range(1, self.NUMBER_OF_NODES+1)}
		for u, v in edges:
			adj[u].append(v)
		return adj

	def get_undirected_acyclic_edges(self):
		# UNDIRECTED - ACYCLIC - EDGES
		edgesUAE = [(1,2), (2,1), (2,4), (4,2), (3,4), (4,3), (3,5), (5,3), (5,6), \
			(6,5), (1,3), (3,1), (4,5), (5,4), (4,6), (6,4)]
		return edgesUAE

	def get_undirected_acyclic_adj(self):
		edges = self.get_undirected_acyclic_edges()
		adj = {x:[] for x in range(1, self.NUMBER_OF_NODES+1)}
		for u, v in edges:
			adj[u].append(v)
		return adj
