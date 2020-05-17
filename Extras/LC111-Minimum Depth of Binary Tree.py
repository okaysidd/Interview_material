"""
111. Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.
Example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
	"""
	Important distinction from the maximum depth.
	If root has both children, return min path between them.
	However, if a root has one child, return min path of only that,
	since if you calculate min of that and the None child, it'll
	always be 0. Thus the non-None node will never be accounted for.
	#NOTE: IMPORATNT!!
	"""
    def minDepth(self, root: TreeNode) -> int:
        if root:
            if root.left == None or root.right == None:
                return 1 + self.minDepth(root.left) + self.minDepth(root.right)
            return min(1 + self.minDepth(root.left), 1 + self.minDepth(root.right))
        else:
            return 0

x = Solution()
a = TreeNode(1)
a.left = TreeNode(2)
# a.left.left = TreeNode(3)
print(x.minDepth(a))
