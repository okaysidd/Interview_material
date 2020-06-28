"""
Graph can be given in many ways. Here just taking the adjencency
list as the input.
The adjecency list will change depending on whether the graph is
directed or undirected. The code remains the same.
Uses of BFS:
- Finding shortest path**
- Solving rubik's cube
- Finding all paths
"""
class BreadthFirstSearch:
	"""
	Choose an arbitrary point of its given as input. The level
	of this node will be 0 and the parent will be null. Maintain
	a level wise list of nodes, and replace it with the next level
	of nodes when one level nodes are exhausted. To avoid getting
	stuck in a cycle, check if the node has already been visited.
	For every node, set the level as an incrementing i and parent
	as the node it was in the list of in the adjacency list.
	Level gives shortest path length from the start point.
	Parent gives the shortest path.
	"""
	def bfs(self, graph, start_point):
		level = {
			start_point: 0
		}
		parent = {
			start_point: None
		}
		frontier = [start_point]
		i = 1
		while frontier:
			next = []
			for node in frontier:
				if nei in graph:
					for nei in graph[node]:
						if nei not in level:
							next.append(nei)
							level[nei] = i
							parent[nei] = node
			i += 1
			frontier = next
		return level, parent


graph = {
	's': ['a', 'b'],
	'a': ['s', 'c'],
	'b': ['s', 'c', 'd'],
	'c': ['a', 'b', 'd', 'e'],
	'd': ['b', 'c', 'e'],
	'e': ['c', 'd']
}
start_point = 's'
x = BreadthFirstSearch()
levels, parents = x.bfs(graph, start_point)
print(f'Levels: {levels}')
print(f'Parents: {parents}')
