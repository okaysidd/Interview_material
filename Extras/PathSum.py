"""
Path Sum
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
Note: A leaf is a node with no children.
Example:
Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	"""
	Awesome solution.
	Subtract root.val from sum at each step and check below whether leaf is
	reached or not. If leaf is reached and the val at leaf == sum asked,
	return True.
	Read it. It is awesome.
	"""
    def hasPathSum(self, root, sum, res=None):
        if root == None:
            return None
        if res == None:
            res = []
        if root.left == None and root.right == None:
            return root.val == sum
			# if root.val == sum:
            #     return True
            # else:
            #     return False
        # if self.hasPathSum(root.left, sum-root.val, res) or self.hasPathSum(root.right, sum-root.val, res):
        #     return True
        # return False
		return self.hasPathSum(root.left, sum-root.val, res) or self.hasPathSum(root.right, sum-root.val, res) # smaller

a = TreeNode(-10)
a.left = TreeNode(9)
a.right = TreeNode(20)
a.right.left = TreeNode(15)
a.right.right = TreeNode(7)

x = Solution()
print(x.hasPathSum(a))
