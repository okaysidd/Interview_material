"""
Maximum XOR of Two Numbers in an Array
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 ≤ i ≤ j < n.
Follow up: Could you do this in O(n) runtime?

Example 1:
Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.

Example 2:
Input: nums = [0]
Output: 0

Example 3:
Input: nums = [2,4]
Output: 6

Example 4:
Input: nums = [8,10,2]
Output: 10

Example 5:
Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127

Constraints:

1 <= nums.length <= 2 * 104
0 <= nums[i] <= 231 - 1
"""
class TrieNode:
	def __init__(self, char):
		self.char = char
		self.completeWord = False
		self.children = []

class Trie:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.root = TrieNode('*')

	def insert(self, word: str) -> None:
		"""
		Inserts a word into the trie.
		"""
		current_node = self.root
		for ch in word:
			found_in_child = False
			for node in current_node.children:
				if node.char == ch:
					found_in_child = True
					current_node = node
					break
			if found_in_child == False: # the ch was not found anywhere
				new_node = TrieNode(ch)
				current_node.children.append(new_node)
				current_node = new_node
		current_node.completeWord = True # since completely inserted hehe
		return
	
	def search(self, word: str, current_node=None) -> bool:
		"""
		Returns if the word is in the trie.
		"""
		if current_node == None:
			current_node = self.root
		for ch in word:
			found_in_child = False
			for node in current_node.children:
				if node.char == ch:
					found_in_child = True
					current_node = node
			if found_in_child == False: # some char not found anywhere
				return False
		if current_node.completeWord:
			return True
		return False
	
	def startsWith(self, prefix: str) -> bool:
		"""
		Returns if there is any word in the trie that starts with the given prefix.
		"""
		current_node = self.root
		for ch in prefix:
			found_in_child = False
			for node in current_node.children:
				if node.char == ch:
					found_in_child = True
					current_node = node
			if found_in_child == False: # some char not found anywhere
				return False
		return True

class Solution:
	"""
	XOR operation => 0 ^ 1 = 1 and 1 ^ 0 = 1. Otherwise 0.
	So insert all the numbers in input (in binary format) to a trie.
	Then traversing from the top, try to switch between 1 and 0 as often as
	possible, to get the maximum XOR.
	Start with 1, this is greedy but works because any number staring with 0
	will definitely be smaller than any number that starts with 1.
	# NOTE: IMPORTANT. GREAT QUESTION. ASKED IN GOOGLE INTERN CODING TEST.
	"""
	def findMaximumXOR(self, nums):
		nums2 = ["{:032b}".format(x) for x in nums]
		x = Trie()
		for n in nums2:
			x.insert(n)
		max_xor = -2**(32)
		for n in nums2:
			i = 0
			temp = ""
			while i < 32:
				if n[i] == "1":
					if x.startsWith(temp + "0"):
						temp += "0"
					else:
						temp += "1"
				else:
					if x.startsWith(temp + "1"):
						temp += "1"
					else:
						temp += "0"
				i += 1
			max_xor = max(max_xor, int(temp, base=2) ^ int(n, base=2))
		return max_xor

nums = [14,70,53,83,49,91,36,80,92,51,66,70]
x = Solution()
print(x.findMaximumXOR(nums))
