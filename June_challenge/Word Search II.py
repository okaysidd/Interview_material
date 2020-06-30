"""
Word Search II
Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:
Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Note:
All inputs are consist of lowercase letters a-z.
The values of words are distinct.
"""
class TrieNode:
	def __init__(self):
		self.children = {}
		self.complete_word = False

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word):
		current_node = self.root
		for ch in word:
			children = current_node.children
			if ch not in children:
				children[ch] = TrieNode() # updating children if ch not present
			current_node.children = children # updating current_node's children with updated children
			current_node = current_node.children[ch]
		current_node.complete_word = True

	def search(self, word):
		current_node = self.root
		for ch in word:
			children = current_node.children
			if ch not in children:
				return False
			current_node = current_node.children[ch]
		if current_node.complete_word == True:
			return True
		return False

class Solution:
	"""
	Compared to Word search, implementation of Trie is required to beat the largest input.
	"""
	def findWords(self, board, words):
		trie = Trie()
		res = []
		self.num_words = len(words)
		for w in words:
			trie.insert(w)
		for i in range(len(board)):
			for j in range(len(board[0])):
				self.bfs(board, i, j, path="", node=trie.root, res=res)
		return res
	
	def bfs(self, board, i, j, path, node, res):
		if self.num_words == 0: return
		if node.complete_word == True:
			node.complete_word = False
			res.append(path)
			self.num_words -= 1
		if i<0 or j<0 or i>=len(board) or j>=len(board[0]):
			return
		temp = board[i][j]
		if temp not in node.children:
			return
		board[i][j] = '#'
		self.bfs(board, i-1, j, path+temp, node.children[temp], res)
		self.bfs(board, i, j-1, path+temp, node.children[temp], res)
		self.bfs(board, i+1, j, path+temp, node.children[temp], res)
		self.bfs(board, i, j+1, path+temp, node.children[temp], res)
		board[i][j] = temp

board = [['o','a','a','n'],
		['e','t','a','e'],
		['i','h','k','r'],
		['i','f','l','v']]
words = ["oath","pea","eat","rain"]

x = Solution()
print(x.findWords(board, words))
