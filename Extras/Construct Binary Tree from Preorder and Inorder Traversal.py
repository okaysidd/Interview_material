"""
Construct Binary Tree from Preorder and Inorder Traversal
Solution
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

	3
   / \
  9  20
	/  \
   15   7
"""
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
class Solution:
	"""
	Same as creating tree from inorder and postorder.
	Changes- pop is from 0 index, not last.
	root.left is set first because preorder is given, and so
	we will start popping from the left.
	"""
	def buildTree(self, preorder, inorder) -> TreeNode:
		if not inorder or not preorder:
			return
		root = TreeNode(preorder.pop(0))
		ind = inorder.index(root.val)
		root.left = self.buildTree(preorder, inorder[:ind])
		root.right = self.buildTree(preorder, inorder[ind+1:])
		return root

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
x = Solution()
print(x.buildTree(preorder, inorder))
