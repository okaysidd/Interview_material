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

# TODO: implement delete, suffix

x = Trie()
words = ['water', 'word', 'walk']
for w in words:
	x.insert(w)
print(x.search('water'))
print(x.search('wate'))
