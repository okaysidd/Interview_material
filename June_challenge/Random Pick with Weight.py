"""
Random Pick with Weight
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:
1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.

Example 1:
Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]

Example 2:
Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
"""
import random
class Solution:
	"""
	Solution I thought to make this work. Creates bucket, searches for random
	number in the buckets created. Time exceeds though. The pick index is slow
	and can be improved with Binary search.
	"""
	def __init__(self, w):
		self.w = w
		total_w = sum(self.w)
		self.res = []
		last = 0
		for weight in self.w:
			self.res.append((last+(weight/total_w), weight))
			last = last+(weight/total_w)

	def pickIndex(self) -> int:
		pick = random.random()
		i = 0
		while 1:
			if self.res[i][0] <= pick:
				i += 1
			else:
				return i

import itertools, bisect, random
class Solution2:
	"""
	Solution that uses in-built libraries, much faster.
	"""
	def __init__(self, w):
		self.w = list(itertools.accumulate(w))
		print(self.w)

	def pickIndex(self):
		return bisect.bisect_left(self.w, random.randint(1, self.w[-1]))

x = Solution([1,2,3,4])
output = [x.pickIndex() for i in range(10000)] # note that it returns index
print(len([g for g in output if g==0]))
print(len([g for g in output if g==1]))
print(len([g for g in output if g==2]))
print(len([g for g in output if g==3]))
