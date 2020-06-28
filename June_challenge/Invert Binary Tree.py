"""
Invert Binary Tree

Example:
Input:

	 4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

	 4
   /   \
  7     2
 / \   / \
9   6 3   1
"""
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
class Solution:
	"""
	Using recursion stack.
	"""
	def invertTree(self, root: TreeNode) -> TreeNode:
		if root:
			root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
			return root

class Solution2:
	"""
	Using explicit stack.
	"""
	def invertTree(self, root: TreeNode) -> TreeNode:
		stack = [root]
		while stack:
			node = stack.pop()
			if node:
				node.left, node.right = node.right, node.left
				stack += node.left, node.right
		return root

a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.left = TreeNode(4)
a.left.right = TreeNode(5)

x = Solution()
print(x.invertTree(a))
