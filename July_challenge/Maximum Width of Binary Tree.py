"""
Maximum Width of Binary Tree
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.
The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:
Input: 
		   1
		 /   \
		3     2
	   / \     \  
	  5   3     9 
Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).

Example 2:
Input: 
		  1
		 /  
		3    
	   / \       
	  5   3     
Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).

Example 3:
Input: 
		  1
		 / \
		3   2 
	   /        
	  5      
Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).

Example 4:
Input: 
		  1
		 / \
		3   2
	   /     \  
	  5       9 
	 /         \
	6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
"""
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
class Solution:
	"""
	Note to self: KNOWING NORMAL BFS/DFS WILL NOT SOLVE EVERYTHING.
	THINK ABOUT PROBLEMS FROM A UNBIASED STANDPOINT IF WHAT YOU ALREADY
	KNOW DOES NOT WORK.
	# NOTE: IMPORTANT!
	"""
	def widthOfBinaryTree(self, root: TreeNode):
		max_width = 0
		def some(node, depth, position, d=None):
			if node == None: return
			if d == None:
				d = {}
			if depth not in d:
				d[depth] = position
			nonlocal max_width
			max_width = max(max_width, position - d[depth] + 1)
			some(node.left, depth+1, position*2, d)
			some(node.right, depth+1, position*2+1, d)

		some(root, 1, 1)
		return max_width

b = TreeNode(37)
b.left = TreeNode(-34)
b.right = TreeNode(-48)
b.left.left = TreeNode(-100)
b.right.left = TreeNode(-100)
b.right.right = TreeNode(48)
b.right.right.left = TreeNode(-54)
b.right.right.left.left = TreeNode(-71)
b.right.right.left.right = TreeNode(-22)
b.right.right.left.right.right = TreeNode(8)

x = Solution()
print(x.widthOfBinaryTree(b))
