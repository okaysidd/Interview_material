"""
Binary Search Trees (BST) - tree structure that follow the search property, ie, for every node, all the nodes in the left subtree are smaller than the current node and all the nodes in the right subtree are larger than the current node.
rank(n) => the rank of a node in a tree is the sum of the number of nodes that its subtrees have, including itself.

		   2 (rank-4)
		  / \
(rank-1) 1   5 (rank-2)
			/
		   3 (rank-1)

Rank will be used in calculating the number of values in the tree that are smaller than or equal to a particular value.
For example-
To find number of nodes smaller than 4
- traverse tree to find where 4 would be inserted
- at every step, if you go right, add the rank of left sub tree (before actually going right)
- at every such step, add 1 to the total, for the current node.
- if you go left, don't add anything

# NOTE: In-order traversal of a BST will give us the sorted list of elements.
Main two important things about BSTs - search and rotation (for balancing the tree).
"""


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.rank = 1

	def add_item(self, root, val):
		current_node = root
		while current_node:
			current_node.rank += 1 # for rank calculation
			if val < current_node.val:
				if current_node.left:
					current_node = current_node.left
				else:
					current_node.left = TreeNode(val)
					break
			else:
				if current_node.right:
					current_node = current_node.right
				else:
					current_node.right = TreeNode(val)
					break
		return root

	def get_nodes_smaller(self, root, val, res=None):
		if res == None:
			res = 0
		if root:
			if val > root.val: # if going to the left
				if root.left: # if the left of root exists
					res += root.left.rank # add the rank of the left subtree, since all the nodes on that left side will be smaller than val
				res += 1 # add 1 for current node
				return self.get_nodes_smaller(root.right, val, res)
			elif val < root.val: # if going to the left, cannot add anything, as we haven't encountered a node smaller than val yet
				return self.get_nodes_smaller(root.left, val, res)
			else:
				if root.left: # if the current node matches value, add the rank of left subtree, as all nodes on left will be smaller
					res += root.left.rank
				return res + 1 # add one for current node, as we check for less than equal to
		return res

	def get_min(self, root):
		if root:
			if root.left:
				return self.get_min(root.left)
			return root.val

	def get_max(self, root):
		if root:
			if root.right:
				return self.get_min(root.right)
			return root.val

a = TreeNode(49)
a.add_item(a, 46)
a.add_item(a, 43)
a.add_item(a, 79)
a.add_item(a, 64)
a.add_item(a, 83)

print(a.get_max(a))
print(a.get_nodes_smaller(a, 79))
