"""
Convert Sorted Array to Binary Search Tree

Solution
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

	  0
	 / \
   -3   9
   /   /
 -10  5
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
	def sortedArrayToBST(self, nums) -> TreeNode:
		if len(nums) == 1:
			return TreeNode(nums[0])
		if len(nums) < 1:
			return
		l, r = 0, len(nums)-1
		mid = (l+r)//2
		root = TreeNode(nums[mid])
		left_subtree = nums[:mid]
		root.left = self.sortedArrayToBST(left_subtree)
		right_subtree = nums[mid+1:]
		root.right = self.sortedArrayToBST(right_subtree)
		return root

nums = [-10,-3,0,5,9]
x = Solution()
print(x.sortedArrayToBST(nums))
