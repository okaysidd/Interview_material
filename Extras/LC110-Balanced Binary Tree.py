"""
110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:
Given the following tree [3,9,20,null,null,15,7]:
	  3
	 / \
	9  20
	  /  \
	 15   7
Return true.

Example 2:
Given the following tree [1,2,2,3,3,null,null,4,4]:

	  1
	 / \
	2   2
   / \
  3   3
 / \
4   4
Return false.
"""
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
class Solution:
	"""
	At each node, depth of left and right should not vary by more
	than one. Therefore, get the max depth for left and right
	subtree at each subnode and compare them for being less than
	two apart.
	"""
	def isBalanced(self, root: TreeNode, res=None) -> bool:
		if res == None:
			res = True
		if root:
			res = res and abs(self.helper(root.right) - self.helper(root.left)) < 2
			return self.isBalanced(root.left, res) and self.isBalanced(root.right, res)
		else:
			return res
	def helper(self, root):
		if root:
			return 1 + max(self.helper(root.left), self.helper(root.right))
		else:
			return 0

a = TreeNode('1')
a.left = TreeNode('2')
a.right = TreeNode('2')
a.left.left = TreeNode('3')
a.right.right = TreeNode('3')
a.left.left.left = TreeNode('4')
a.right.right.right = TreeNode('4')

x = Solution()
print(x.isBalanced(a))
