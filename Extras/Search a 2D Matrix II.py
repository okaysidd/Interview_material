"""
Search a 2D Matrix II
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example:
Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.
Given target = 20, return false.
"""
class Solution:
	"""
	Good question.
	Start from one end of row/column and 0 of other.
	Reduce/increase as you move left/up.
	"""
	def searchMatrix(self, matrix, target):
		if len(matrix) == 0 or len(matrix[0]) == 0:
			return False
		i, j = len(matrix)-1, 0
		while i >= 0 and j < len(matrix[0]):
			print(i, j)
			curr = matrix[i][j]
			if target > curr:
				j += 1
			elif target < curr:
				i -= 1
			else:
				return (i, j)
			print(i, j)
		return -1

matrix = [[1,   4,  7, 11, 15],
		  [2,   5,  8, 12, 19],
		  [3,   6,  9, 16, 22],
		  [10, 13, 14, 17, 24],
		  [18, 21, 23, 26, 30]]
target = 17

x = Solution()
print(x.searchMatrix(matrix, target))
