"""
Diameter of Binary Tree
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode, d={}) -> int:
        max_ = 0
        if not root:
            return max_
        if root.left in d.keys():
            h_left = d[root.left]
        else:
            h_left = self.height(root.left)
            d[root.left] = h_left
        if root.right in d.keys():
            h_right = d[root.right]
        else:
            h_right = self.height(root.right)
            d[root.right] = h_right
        total_height = h_left + h_right
        max_ = max(total_height, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max_
    def height(self, a, m=0, c=0):
        if not a:
            m = max(c, m)
            return m
        c += 1
        return max(self.height(a.left, m, c), self.height(a.right, m, c))

a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
a.left.left = TreeNode(4)
a.left.right = TreeNode(5)
a.left.left.left = TreeNode(6)
a.left.left.right = TreeNode(7)
a.left.left.left.left = TreeNode(8)
b = Solution()
print(b.diameterOfBinaryTree(a))
