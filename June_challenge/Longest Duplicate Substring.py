"""
Longest Duplicate Substring
Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)
Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)

Example 1:
Input: "banana"
Output: "ana"

Example 2:
Input: "abcd"
Output: ""

Note:
2 <= S.length <= 10^5
S consists of lowercase English letters.
"""
class Solution:
	"""
	Uses Rabin Karp (rolling hashes) combined with Binary search to avoid
	checking for all substrings.
	If the largest duplicate substring of length 10 exsits, duplicate substrings
	of lenght 9,8,.. will exist as well. So we check for a middle number and
	if found, find for bigger numbers, and lesser numbers if not found, and so on.
	Don't know what is happenning in Rabin Karp hash calculation process.
	"""
	def longestDupSubstring(self, S):
		p = 2**63-1
		def rabinKarp(mid):
			current_hash = 0
			for i in range(mid):
				current_hash = (current_hash*26 + nums[i]) % p
			hashes = {current_hash}
			pos = -1
			max_pow = pow(26, mid, p)
			for i in range(mid, len(S)):
				current_hash = (current_hash * 26 - nums[i-mid]*max_pow + nums[i]) % p
				if current_hash in hashes:
					pos = i - mid + 1
				hashes.add(current_hash)
			return pos

		nums = [ord(c) for c in S]
		l = 0
		r = len(S)
		res = ''
		while l+1<r:
			mid = (l+r)//2
			pos = rabinKarp(mid)
			if pos == -1:
				r = mid
			else:
				res = max(res, S[pos:pos+mid], key=len)
				l = mid
		return res

S = 'banana'
x = Solution()
print(x.longestDupSubstring(S))
