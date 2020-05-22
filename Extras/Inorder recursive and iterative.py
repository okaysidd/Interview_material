class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Solution:
	def inorder_rec(self, root):
		"""
		Recursive. The stack is maintained by the language for us.
		In this easy to understand way, we just call for the left
		subtree, read the root and call for the right subtree recursively.
		"""
		res = []
		def helper(root, res):
			if root:
				helper(root.left, res)
				res.append(root.val) # can append node or only its val, based on use
				helper(root.right, res)
			return res
		return helper(root, res)
	
	def inorder_iter(self, root):
		"""
		Iterative. We maintain the stack. Keep pushing all left. When
		null pop if no right. Then print the root.
		"""
		stack = []
		res = []
		while True: # the break condition will be inside the loop
			if root:
				stack.append(root)
				root = root.left
			elif stack:
				root = stack.pop()
				res.append(root.val)
				root = root.right
			else:
				break
		return res

a = TreeNode(3)
a.left = TreeNode(1)
a.right = TreeNode(4)
a.left.right = TreeNode(2)
x = Solution()
print(x.inorder_rec(a))
print(x.inorder_iter(a))
