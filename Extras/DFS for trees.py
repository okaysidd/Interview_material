"""
DFS for trees is basically of three types:
Preorder (root, left, right)
Inorder (left, root, right)
Postorder (left, right, root)
"""
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class DepthFirstSearch:
	"""
	Pick a node and one of its child and repeat. Go as deep as possible
	and then backtrack and go to another child. The stack is implicitly
	handled by the recursion stack.
	"""
	def preorder(self, root):
		order = []
		def helper(root):
			nonlocal order
			if root:
				order.append(root.val)
				helper(root.left)
				helper(root.right)
		helper(root)
		return order

	def inorder(self, root):
		order = []
		def helper(root):
			nonlocal order
			if root:
				helper(root.left)
				order.append(root.val)
				helper(root.right)
		helper(root)
		return order

	def postorder(self, root):
		order = []
		def helper(root):
			nonlocal order
			if root:
				helper(root.left)
				helper(root.right)
				order.append(root.val)
		helper(root)
		return order

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

x = DepthFirstSearch()
print(x.preorder(root))
print(x.inorder(root))
print(x.postorder(root))
