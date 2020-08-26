"""
Find the Winner of an Array Game
Given an integer array arr of distinct integers and an integer k.
A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0 and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.
Return the integer which will win the game.
It is guaranteed that there will be a winner of the game.

Example 1:
Input: arr = [2,1,3,5,4,6,7], k = 2
Output: 5
Explanation: Let's see the rounds of the game:
Round |       arr       | winner | win_count
  1   | [2,1,3,5,4,6,7] | 2      | 1
  2   | [2,3,5,4,6,7,1] | 3      | 1
  3   | [3,5,4,6,7,1,2] | 5      | 1
  4   | [5,4,6,7,1,2,3] | 5      | 2
So we can see that 4 rounds will be played and 5 is the winner because it wins 2 consecutive games.

Example 2:
Input: arr = [3,2,1], k = 10
Output: 3
Explanation: 3 will win the first 10 rounds consecutively.

Example 3:
Input: arr = [1,9,8,2,3,7,6,4,5], k = 7
Output: 9

Example 4:
Input: arr = [1,11,22,33,44,55,66,77,88,99], k = 1000000000
Output: 99
"""
class Solution:
	"""
	Bad way of doing it.
	"""
	def getWinner(self, arr, k):
		if k > len(arr): return max(arr)
		res = [0 for x in arr]
		i = 0
		j = 0
		while i <= len(arr) and j < len(arr)-1:
		    if arr[j] > arr[j+1]:
		        res[j] += 1
		        if res[j] == k:
		            return arr[j]
		        arr[j], arr[j+1] = arr[j+1], arr[j]
		        res[j], res[j+1] = res[j+1], res[j]
		        j += 1
		    else:
		        res[j+1] += 1
		        if res[j+1] == k:
		            return arr[j+1]
		        j += 1
		    i += 1
		return arr[j]

class Solution2:
	"""
	Good way of doing it. Maintain a current number, and win count.
	For each number greater than previous, current will be set to new
	number and win counter will be reset.
	If win reaches k, return current.
	"""
	def getWinner(self, arr, k):
		win, current = 0, arr[0]
		for i in range(1, len(arr)):
			if arr[i] > current:
				current = arr[i]
				win = 0
			win += 1
			if win == k:
				break
		return current

arr = [2,1,3,5,4,6,7]
k = 2
x = Solution()
print(x.getWinner(arr, k))
