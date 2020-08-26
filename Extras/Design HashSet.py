"""
Design HashSet
Design a HashSet without using any built-in hash table libraries.
To be specific, your design should include these functions:
add(value): Insert a value into the HashSet. 
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:
MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)

Note:
All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.
"""
class MyHashSet:
	"""
	Uses chaining hashing.
	"""
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		# initializing large array
		self.hash = [[] for _ in range(1<<15)]
		
	def eval_hash(self, key):
		# using universal hashing (Multiplicative Hash)
		return ((key*1031237) & (1<<20) - 1)>>5
	
	def add(self, key: int) -> None:
		bucket = self.eval_hash(key)
		if key not in self.hash[bucket]:
			self.hash[bucket].append(key)
		return True
	
	def remove(self, key: int) -> None:
		bucket = self.eval_hash(key)
		if key in self.hash[bucket]:
			self.hash[bucket].remove(key)
			return True
		return False
		
	def contains(self, key: int) -> bool:
		"""
		Returns true if this set contains the specified element
		"""
		bucket = self.eval_hash(key)
		if key in self.hash[bucket]:
			return True
		return False
		
# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
key = 34
print(obj.add(key))
# print(obj.hash)
print(obj.remove(key))
param_3 = obj.contains(key)
print(param_3)
