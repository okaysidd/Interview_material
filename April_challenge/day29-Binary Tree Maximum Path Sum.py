"""
124. Binary Tree Maximum Path Sum
Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:
Input: [1,2,3]
	   1
	  / \
	 2   3
Output: 6

Example 2:
Input: [-10,9,20,null,null,15,7]
   -10
   / \
  9  20
	/  \
   15   7
Output: 42
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
	"""
	This is a tricky one, because if the path contains of a particular
	root, its left and its right, then the result will be sum of all of
	them. However if that node is just in the passage of another, the result
	will add that node and the maximum gain from either the left or the
	right subtree.
	This explains it in a great way-
	https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram
	"""
	def maxPathSum(self, root: TreeNode) -> int:
		max_sum = -9999999
		def get_max_sum(node):
			nonlocal max_sum
			if not node:
				return 0
			left_gain = max(get_max_sum(node.left), 0) # max with zero because if the subtree provides negative gain, we take none
			right_gain = max(get_max_sum(node.right), 0)

			max_sum = max(max_sum, node.val + left_gain + right_gain) # maintain sum if that complete path (root+left+right) are used

			return node.val + max(left_gain, right_gain) # returns node + max of left/right because this will be in path of other path

		get_max_sum(root)
		return max_sum

a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)

x = Solution()
print(x.maxPathSum(a))
