"""
Surrounded Regions
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X

Explanation:
Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""
class Solution:
	"""
	Not the best solution, find all islands ('O') that start with/touch the
	border, and flip them to 'B'. Then flip all other 'O' to 'X' and all 'B'
	to 'X'.
	Another way to think about it- we have to find all the 'O' cells that
	do not have a path to the border elements.
	"""
	def solve(self, board):
		"""
		Do not return anything, modify board in-place instead.
		"""
		for i in range(len(board)):
			for j in range(len(board[0])):
				if i in {0, len(board)-1} or j in {0, len(board[0])-1} and board[i][j] == 'O':
					self.BFS_X(board, i, j, 'B')
		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j] == 'O':
					board[i][j] = 'X'
				elif board[i][j] == 'B':
					board[i][j] = 'O'
		return board
					
	def BFS_X(self, board, i, j, flip):
		if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j] != 'O':
			return
		board[i][j] = flip
		self.BFS_X(board, i-1, j, flip)
		self.BFS_X(board, i, j-1, flip)
		self.BFS_X(board, i+1, j, flip)
		self.BFS_X(board, i, j+1, flip)

board = [
	['X', 'X', 'X', 'X'],
	['X', 'O', 'O', 'X'],
	['X', 'X', 'O', 'X'],
	['X', 'O', 'X', 'X'],
]
x = Solution()
print(x.solve(board))
