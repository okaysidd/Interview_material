"""
Word Search
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

Constraints:
board and word consists only of lowercase and uppercase English letters.
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
"""
class Solution:
	"""
	Compared to Word search ii, this can be done using find-islands type solution.
	"""
	def exist(self, board, word):
		visited = [[0 for x in board[0]] for y in board]
		def bfs(board, i, j, word, visited, index):
			if index == len(word):
				return True
			if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or visited[i][j] == 1 or word[index] != board[i][j]:
				return False
			visited[i][j] = 1
			index += 1
			res = any([bfs(board, i-1, j, word, visited, index), \
				   bfs(board, i, j-1, word, visited, index), \
				   bfs(board, i+1, j, word, visited, index), \
				   bfs(board, i, j+1, word, visited, index)])
			if res:
				return res
			visited[i][j] = 0
			return False
		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j] == word[0]:
					if bfs(board, i, j, word, visited, index=0):
						return True
		return False

board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED"
x = Solution()
print(x.exist(board, word))
