"""
Number of Good Leaf Nodes Pairs
Given the root of a binary tree and an integer distance. A pair of two different leaf nodes of a binary tree is said to be good if the length of the shortest path between them is less than or equal to distance.
Return the number of good leaf node pairs in the tree.

Example 1:
Input: root = [1,2,3,null,4], distance = 3
Output: 1
Explanation: The leaf nodes of the tree are 3 and 4 and the length of the shortest path between them is 3. This is the only good pair.

Example 2:
Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The pair [4,6] is not good because the length of ther shortest path between them is 4.

Example 3:
Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
Output: 1
Explanation: The only good pair is [2,5].

Example 4:
Input: root = [100], distance = 1
Output: 0

Example 5:
Input: root = [1,1,1], distance = 2
Output: 1
"""
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
class Solution:
	"""
	Traversing from the bottom up, post order, keep note of left and right nodes'
	height from the leaves. While moving every step above, add the left and right
	values and add 1, signifying any common ancestor of a leaf above this node
	will have at least this height.
	Visit: https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/discuss/755767/Python-Postorder-Traversal
	# NOTE: IMPORTANT!
	"""
	def countPairs(self, root: TreeNode, distance: int) -> int:
		count = 0
		def dfs(node):
			nonlocal count, distance
			if node == None: return []
			if node.left == None and node.right == None: return [1] # leaf node, so just one edge away
			left = dfs(node.left)
			right = dfs(node.right)
			if left and right:
				count += sum(i + j <= distance for i in left for j in right)
			return [n+1 for n in left+right if n+1<distance] # leave out values more than distance, since they won't add value later
		dfs(root)
		return count

a = TreeNode(1)
a.left = TreeNode(2)
a.left.left = TreeNode(4)
a.left.right = TreeNode(4)
a.right = TreeNode(3)
a.right.left = TreeNode(6)
a.right.right = TreeNode(7)

distance = 3

x = Solution()
print(x.countPairs(a, distance))
