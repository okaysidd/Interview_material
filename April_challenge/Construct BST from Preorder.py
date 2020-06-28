"""
Construct Binary Search Tree from Preorder Traversal
Return the root node of a binary search tree that matches the given preorder traversal.
(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

Example 1:
Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

Note: 
1 <= preorder.length <= 100
The values of preorder are distinct.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder):
        root = TreeNode(preorder[0])
        for current_val in preorder[1:]:
            node = TreeNode(current_val)
            self.create_BST(root, node)
        return root
    def create_BST(self, root, node):
        if node.val < root.val:
            if root.left == None:
                root.left = node
            else:
                self.create_BST(root.left, node)
        else:
            if root.right == None:
                root.right = node
            else:
                self.create_BST(root.right, node)

preorder = [8,5,1,7,10,12]
a = Solution()
print(a.bstFromPreorder(preorder))
