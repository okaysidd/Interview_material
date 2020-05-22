"""
Maximal Square
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:
Input: 
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Output: 4
"""
class Solution:
	"""
	Create a dp matrix which has one extra upper row and one extra left column.
	Now moving from [1][1], each cell is only as strong as the minimum value
	around it. Thus, replace each cell, that is one, with minimum value around
	it (up, left and diagonal up-left) + 1 (for the value of the current cell).
	Maximum number in all the grid can be tracked as we move and that will be
	length of side of the largest square. Area, square of that length.
	Noice explanation-
	https://leetcode.com/problems/maximal-square/discuss/600149/Python-Thinking-Process-Diagrams-DP-Approach
	"""
	def maximalSquare(self, matrix) -> int:
		if len(matrix) == 0:
			return 0
		dp = [[0 for i in range(len(matrix[0])+1)] for j in range(len(matrix)+1)]
		max_ = 0
		for i in range(1, len(dp)):
			for j in range(1, len(dp[0])):
				if matrix[i-1][j-1] == '1':
					dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
					max_ = max(max_, dp[i][j])
		return max_ * max_

class Solution2:
	"""
	Solution without requiring the extra space of dp matrix, but alters the
	input matrix, so trade-offs.
	In the same matrix, for the 0 row and 0 column, just update the max_ in case
	there is a '1' at the cell.
	For other rows and columns, if cell has 1, take the min of its preceding
	(up, left and diagonal up-left) and add the current cell to it (1). Keep
	track of max encountered.
	"""
	def maximalSquare(self, matrix) -> int:
		if len(matrix) == 0:
			return 0
		max_ = 0
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				if matrix[i][j] == '1':
					if i == 0 or j == 0:
						max_ = max(max_, int(matrix[i][j]))
					else:
						matrix[i][j] = min(int(matrix[i-1][j]), int(matrix[i][j-1]), int(matrix[i-1][j-1])) + 1
						max_ = max(max_, matrix[i][j])                        
		return max_ * max_

a = Solution()
matrix = [['1', '0', '1', '0', '0'],
		  ['1', '0', '1', '1', '1'],
		  ['1', '1', '1', '1', '1'],
		  ['1', '0', '1', '1', '0']]
print(a.maximalSquare(matrix))
