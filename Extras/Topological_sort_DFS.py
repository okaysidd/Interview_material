class DFS_recursive:
	def Topological_sort(self, graph):
		result = []
		def dfs_visit(node):
			for neighbor in graph[node]:
				if neighbor not in seen:
					seen.add(neighbor)
					dfs_visit(neighbor)
			result.append(node)
		seen = set()
		values = [v for v in graph.values()]
		# for v in graph.values():
		# 	values.extend(v)
		for node in graph:
			if node not in values:
				if node not in seen:
					dfs_visit(node)
		return result[::-1]
	
	def DFS_with_cycle_check(self, graph):
		BACK_EDGE = False
		def dfs_visit(node, result=None, current_stack=None):
			if current_stack and node in current_stack:
				nonlocal BACK_EDGE
				BACK_EDGE = True
			if current_stack == None: current_stack = set()
			current_stack.add(node)
			if result == None: result = []
			for neighbor in graph[node]:
				if neighbor not in seen:
					current_stack.add(node)
					result.append(neighbor)
					seen.add(neighbor)
					dfs_visit(neighbor, result, current_stack)
			current_stack = set()
			return result
		parent = {}
		for node in graph:
			seen = set()
			parent[node] = dfs_visit(node)
		return parent, BACK_EDGE

	def DFS(self, graph):
		def dfs_visit(node, result=None):
			if result == None: result = []
			for neighbor in graph[node]:
				if neighbor not in seen:
					result.append(neighbor)
					seen.add(neighbor)
					dfs_visit(neighbor, result)
			return result
		parent = {}
		for node in graph:
			seen = set()
			parent[node] = dfs_visit(node)
		return parent

from Input_for_graphs import GraphInput
a = GraphInput()
graph = a.get_directed_acyclic_adj()
# graph = a.get_directed_cyclic_adj()
# graph[3].append(3)
graph = {'A':['C','D'], 'B':['A','D','G'], 'C':[], 'D':['E','F'], 'E':[], 'F':['C'], 'G':['D']}

x = DFS_recursive()
dfs_route = x.DFS(graph)
print(dfs_route)
dfs_route, cyclic = x.DFS_with_cycle_check(graph)
print(dfs_route)
if not cyclic:
	print(x.Topological_sort(graph))
else:
	print('Not DAG')
