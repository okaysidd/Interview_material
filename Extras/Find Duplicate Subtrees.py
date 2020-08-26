"""
Find Duplicate Subtrees
Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.
Two trees are duplicate if they have the same structure with same node values.

Example 1:

		1
	   / \
	  2   3
	 /   / \
	4   2   4
	   /
	  4
The following are two duplicate subtrees:

	  2
	 /
	4
and

	4
Therefore, you need to return above trees' root in the form of a list.
"""
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
class Solution:
	"""
	Pretty good question, involves designing keys for the required purpose.
	Shows the scope of use of the dictionaries.
	"""
	def findDuplicateSubtrees(self, root: TreeNode):
		res = []
		def some(root, d=None):
			if d == None: d = {}
			if root:
				uid = (root.val, some(root.left, d), some(root.right, d))
				if uid in d:
					d[uid] += 1
					if d[uid] == 2:
						res.append(root)
				else:
					d[uid] = 1
				return uid
		some(root)
		return res

a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.left = TreeNode(4)
a.right.left = TreeNode(2)
a.right.right = TreeNode(4)
a.right.left.left = TreeNode(4)

x = Solution()
print(x.findDuplicateSubtrees(a))
