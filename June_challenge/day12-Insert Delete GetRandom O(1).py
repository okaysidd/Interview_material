"""
Insert Delete GetRandom O(1)
Design a data structure that supports all following operations in average O(1) time.
insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

Example:
// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();
// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);
// Returns false as 2 does not exist in the set.
randomSet.remove(2);
// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);
// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();
// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);
// 2 was already in the set, so return false.
randomSet.insert(2);
// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
"""
import random
class RandomizedSet:
	"""
	Some efforts have to be put to make the data structure(s) insert,
	remove and getRandom all in O(1) time.
	For initializing:
	Initialize a dict (map), a list and a list_length counter.
	For inserting:
	Check if the dict already has the val, if so return False.
	Else add to the list to the last, **as per the length according to the
	array length counter**. Add the val to the dict, with its index as its
	value. Return True
	For removing:
	Check if the val exists in the dict, if not, return False.
	Else check its index from the dict, in the list, move the **last element
	in the list, according to the array_length counter** to this vacant spot
	now and pop it from the dict as well.
	For getRandom:
	Get the random choice from the range 0->array_length counter, pick that
	index from the list to return the number.
	"""

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.map = {}
		self.array = []
		self.array_length = 0

	def insert(self, val: int) -> bool:
		"""
		Inserts a value to the set. Returns true if the set did not already contain the specified element.
		"""
		if val in self.map:
			return False
		try:
			self.array[self.array_length] = val
		except IndexError:
			self.array.append(val)
		self.map[val] = len(self.array)-1
		self.array_length += 1
		return True

	def remove(self, val: int) -> bool:
		"""
		Removes a value from the set. Returns true if the set contained the specified element.
		"""
		if val not in self.map:
			return False
		index = self.map[val]
		if self.array_length > 0:
			self.array[index] = self.array[self.array_length-1]
		self.array_length -= 1
		self.map[self.array[index]] = index
		self.map.pop(val)
		return True

	def getRandom(self) -> int:
		"""
		Get a random element from the set.
		"""
		random_int = random.choice(range(0,self.array_length))
		return self.array[random_int]

input1 = ["RandomizedSet","insert","insert","remove","insert","insert","insert","remove","remove","insert","remove","insert","insert","insert","insert","insert","getRandom","insert","remove","insert","insert"]
input2 = [[],[3],[-2],[2],[1],[-3],[-2],[-2],[3],[-1],[-3],[1],[-2],[-2],[-2],[1],[],[-2],[0],[-3],[1]]
for i, j in zip(input1, input2):
	if i == 'RandomizedSet':
		print('start')
		a = RandomizedSet()
	elif i == 'insert':
		print(f'insert {j[0]}')
		print(a.insert(j[0]))
	elif i == 'remove':
		print(f'remove {j[0]}')
		print(a.remove(j[0]))
	else:
		print('random')
		print(a.getRandom())
	print(a.map)
	print(a.array)
	print(a.array_length)
	print()
	