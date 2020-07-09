"""
204. Count Primes
Count the number of prime numbers less than a non-negative number, n.

Example:
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
class Solution:
	"""
	This is an important question.
	Instead of checking if all numbers are prime or not, make a list
	and eliminate all non prime numbers by marking multiples of smaller
	prime numbers, starting from 2.
	# NOTE: IMPORTANT
	https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
	"""
	def countPrimes(self, n: int) -> int:
		p = [0] * n
		res = 0
		for i in range(2, len(p)):
			if p[i] == 0:
				res+=1
				k = 1
				while i*k < len(p):
					p[i*k] = 1
					k += 1
		return res

n = 1000000
x = Solution()
print(x.countPrimes(n))
