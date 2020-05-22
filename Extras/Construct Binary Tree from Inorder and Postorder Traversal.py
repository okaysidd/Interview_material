"""
Construct Binary Tree from Inorder and Postorder Traversal
Solution
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
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
	# NOTE: Important to note here are lines A and B.
	Since this is postorder we are dealing with, the right subtree will have
	to be called before left as it is post order and we will be popping from
	the right. If interchanged, the postorder pop won't be found in the
	inorder list.
	"""
	def buildTree(self, inorder, postorder) -> TreeNode:
		if len(inorder) == 0 or len(postorder) == 0:
			return None
		root = TreeNode(postorder.pop())
		root_index = inorder.index(root.val)
		root.right = self.buildTree(inorder[root_index+1:], postorder) # line A
		root.left = self.buildTree(inorder[:root_index], postorder) # line B
		return root

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
x = Solution()
print(x.buildTree(inorder, postorder))
"""
Lines A and B use up extra O(n) space, since slicing creates a new list every
time. That can be avoided by using a pointer to mid position, by using a dict.
"""
