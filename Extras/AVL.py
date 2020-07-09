"""
AVL trees (named after inventors Adelson-Velsky and Landis) are self-balancing binary search tree (BST).

Height of a node in a binary tree = 1 + max(height(left_subtree), height(right_subtree))

Main two important things about BSTs are used here - search and rotation (for balancing the tree).
Left rotate:
- root moves to its own left child position
- right child becomes the parent
- left child of right child of original parent becomes right child of now left child of new parent
- original parent retains its left child
- new parent retains its right child
# NOTE: This does not disturb the search property.

		x				y
	   / \			   / \
	  A   y		=>	  x   C
		 / \		 / \
		B   C		A   B
In order traversals:
	  AxByC			  AxByC

Right rotate:
- root moves to its own right child position
- left child becomes the parent
- right child of left child of original parent becomes left child of now right child of new parent
- original parent retains its right child
- new parent retains its left child

		x				y
	   / \			   / \
	  A   y		<=	  x   C
		 / \		 / \
		B   C		A   B
In order traversals:
	  AxByC			  AxByC

# TODO:
- Create AVL tree with insert, delete min and delete features. Rotation will be used to balance the trees. Heights will be stored at each step.
- Get successor and predecessor.
"""
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.height = 0

	def insert(self, root, val):
		if root:
			root.height += 1 # not okay to increment height here because not every insertion will increase overall height
			if val < root.val:
				if root.left:
					root.left.height += 1
					self.insert(root.left, val)
				else:
					root.left = TreeNode(val)
			else:
				if root.right:
					root.right.height += 1
					self.insert(root.right, val)
				else:
					root.right = TreeNode(val)
		print(f'Inserted - {val}')
		print('Checking if balanced..')
		# balanced = self.check_balanced(root)
		# print(balanced)
		while not self.check_balanced(root):
			self.balance_tree(root)
			print('Balanced')

	def check_balanced(self, root):
		if root:
			if root.left and root.right and abs(root.left.height - root.right.height) > 1:
				return False
			self.check_balanced(root.left)
			self.check_balanced(root.right)
			return True

	def balance_tree(self, root):
		pass

	def delete(self, root, val=None):
		if val == None:
			# delele min
			pass
	
		else:
			# delete val
			pass

	def get_sorted(self, root):
		result = []
		def inorder(node):
			if node:
				inorder(node.left)
				result.append(node.val)
				inorder(node.right)
		inorder(root)
		return result

	def get_predecessor(self, root, val):
		pass

	def get_successor(self, root, val):
		pass

if __name__ == "__main__":	
	a = TreeNode(49)
	nums = [43, 26, 77, 89, 13, 23, 18, 7, 52]
	for val in nums:
		print(f'Adding {val}')
		a.insert(a, val)
		print(a.get_sorted(a))

	print('\nPredecessor/Successor of 26')
	print(a.get_predecessor(a, 26))
	print(a.get_successor(a, 26))

	print('\nHeight')
	print(a.height)

	print('\nDelete node min and 43')
	print(a.delete(a)) # min
	print(a.delete(a, 43)) # val

	print('Get all elements in sorted fashion.')
	print(a.get_sorted(a))
