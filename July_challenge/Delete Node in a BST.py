"""
Delete Node in a BST
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:
Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:
root = [5,3,6,2,4,null,7]
key = 3

	5
   / \
  3   6
 / \   \
2   4   7
Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
	5
   / \
  4   6
 /     \
2       7
Another valid answer is [5,2,6,null,4,null,7].
	5
   / \
  2   6
   \   \
	4   7
"""
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	"""
	Searching for the node is straight forward.
	If the node is found and:
	- the node has no children, just remove the node
	- the node has only left or only right child, just replace node with child
	- If both children are present, replace the node with the node that is placed at
		one right, then extreme left of the current node.

	# NOTE: IMMPORTANT!
	"""
	def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
		if not root: return None
		
		if root.val == key:
			if not root.right:
				return root.left
			if not root.left:
				return root.right
			if root.right and root.left:
				temp = root.right
				while temp.left:
					temp = temp.left
				root.val = temp.val
				root.right = self.deleteNode(root.right, root.val)
		elif root.val > key:
			root.left = self.deleteNode(root.left, key)
		else:
			root.right = self.deleteNode(root.right, key)

		return root

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

x = Solution()
print(x.deleteNode(root, 3))
