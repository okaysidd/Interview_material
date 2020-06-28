"""
Sum Root to Leaf Numbers
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
An example is the root-to-leaf path 1->2->3 which represents the number 123.
Find the total sum of all root-to-leaf numbers.
Note: A leaf is a node with no children.

Example:
Input: [1,2,3]
	1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.

Example 2:
Input: [4,9,0,5,1]
	4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
		
class Solution:
	def sumNumbers(self, root: TreeNode) -> int:
		if root == None:
			return 0
		result = []
		res_all = []
		def dfs(root):
			nonlocal result
			if root:
				result.append(root.val)
				if root.left:
					dfs(root.left)
				if root.right:
					dfs(root.right)
			if root and root.left == None and root.right == None:
				nonlocal res_all
				x = result.copy()
				res_all.append(x)
			result.pop()
		dfs(root)
		return sum([int(w) for w in [''.join(z) for z in [[str(y) for y in x] for x in res_all]]])

a = TreeNode(4)
a.left = TreeNode(9)
a.left.left = TreeNode(5)
a.left.right = TreeNode(1)
a.right = TreeNode(0)

x = Solution()
print(x.sumNumbers(a))
