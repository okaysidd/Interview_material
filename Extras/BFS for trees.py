"""
BFS for trees involves visiting the nodes of the tree
level by level.
"""
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class BreadthFirstSearch:
	def bfs(self, root, nodes=None):
		frontier = [root]
		level = {root.val: 0}
		parent = {root.val: None}
		i = 1
		while frontier:
			for node in frontier:
				for f in frontier:
					print(f.val)
				next = []
				if node.left != None:
					level[node.left.val] = i
					next.append(node.left)
					parent[node.left.val] = node.val
				if node.right != None:
					level[node.right.val] = i
					next.append(node.right)
					parent[node.right.val] = node.val
			frontier = next
			i += 1
		return parent, level

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

x = BreadthFirstSearch()
print(x.bfs(root))
