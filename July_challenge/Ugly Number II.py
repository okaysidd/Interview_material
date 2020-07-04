"""
Ugly Number II
Write a program to find the n-th ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note:  
1 is typically treated as an ugly number.
n does not exceed 1690.
"""
class Solution:
	"""
	Maintain how many ugly number have been generated from each of the factors
	in the start list.
	https://leetcode.com/problems/ugly-number-ii/discuss/718879/Python-O(n)-universal-dp-solution-explained
	That way each time we get the next ugly number, making sure we're not getting
	any duplicates or leaving some multiple out.
	"""
	def nthUglyNumber(self, n):
		k, factors = 3, [2,3,5]
		start, numbers = [0,0,0], [1]
		for i in range(n-1):
			candidates = []
			j = 0
			for i in range(k):
				candidates.append(factors[i] * numbers[start[j]])
				j += 1
			new_num = min(candidates)
			numbers.append(new_num)
			for i in range(k):
				if new_num == candidates[i]:
					start[i] += 1
		return numbers[-1]

n = 137
x = Solution()
print(x.nthUglyNumber(n))
