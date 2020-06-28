"""
Remove K Digits
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.
Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""
"""
# NOTE: This problem can be solved two ways. Both greedy.
1) Greedy algorithm in which we maintain a stack that adds elements
	if they are smaller than the peek value (thus greedy) for k times
	only.
2) One without stack finding and removing peaks starting from the left
	hand side. This	is basically greedy too, just accomplishes without
	an explicit stack.
"""
class Solution:
	"""
	# NOTE: IMPORTANT! 
	This greedy uses stack to keep track of peeks.
	Store first element in the empty stack.
	From then, if the next num is smaller than the stack peek and we have
	k to spare, pop from the stack and check next peek too, till the next
	num is not smaller than stack peek.
	Then append.
	Important cases:
	1) '111111' and k = n. No numbers will be removed.
	2) '1234567' and k = n. No peaks so no numbers will be removed here too.
	In both cases, the complete num will get transfered to the stack and k
	will remain untouched. Clearly these cases happen only in sorted list
	(or sub list).
	Thus remove k elements from the right hand side and return.
	"""
	def removeKdigits(self, num: str, k: int) -> str:
		st = []
		i = 0
		while i < len(num):
			if len(st) == 0:
				st.append(num[i])
			elif st and int(st[-1]) > int(num[i]) and k > 0:
				st.pop(-1)
				k -= 1
				i -= 1 # since i is incremented everytime, and this time we don't
				# want that, decreasing it here to negate the increment.
			else:
				st.append(num[i])
			i += 1
		if k:
			st = st[:-k] # for the special sorted cases
		return ''.join(st).lstrip('0') or '0' # removing leading zeros

num = "1432219"
num = "1111111"
k = 3
x = Solution()
print(x.removeKdigits(num, k))
