"""
Letter Combinations of a Phone Number
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# NOTE: IMPORTANT!
"""
class Solution:
	"""
	Instead of:
	for i in ...:
		for j in ..:
			for k in ...:
				....
	for each digit in the input, we use recursion to hold on of them and recurse over the next
	possible set of num-letter mappings first.
	"""
	def letterCombinations(self, digits):
		res = []
		def back(nums, comb):
			phone = {'2': ['a', 'b', 'c'],
					'3': ['d', 'e', 'f'],
					'4': ['g', 'h', 'i'],
					'5': ['j', 'k', 'l'],
					'6': ['m', 'n', 'o'],
					'7': ['p', 'q', 'r', 's'],
					'8': ['t', 'u', 'v'],
					'9': ['w', 'x', 'y', 'z']}
			if len(nums) == 0:
				nonlocal res
				res.append(comb)
			else:
				for letter in phone[nums[0]]:
					back(nums[1:], comb + letter)
		back(digits, "")
		return res

digits = '23'
x = Solution()
print(x.letterCombinations(digits))
