"""
Permutations
Given a collection of distinct integers, return all possible permutations.
Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
# NOTE: IMPORTANT!
"""
class Solution:
	"""
	Everytime take a i value from the nums and append to p, and call
	backtrack funtion with the new values of N and p.
	"""
	def permute(self, nums):
		result = []
		def backtrack(N, p):
			if len(N) == 0:
				nonlocal result
				result.append(p)
			else:
				for i in N:
					new_p = p.copy()
					new_p.append(i)
					left_N = N.copy()
					left_N.remove(i)
					backtrack(left_N, new_p)
		backtrack(nums, [])
		return result

nums = [1,2,3]
x = Solution()
print(x.permute(nums))
