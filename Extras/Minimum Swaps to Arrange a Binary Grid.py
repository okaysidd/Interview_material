"""
Minimum Swaps to Arrange a Binary Grid
Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.
A grid is said to be valid if all the cells above the main diagonal are zeros.
Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.
The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).

Example 1:
Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
Output: 3

Example 2:
Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
Output: -1
Explanation: All rows are similar, swaps have no effect on the grid.

Example 3:
Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
Output: 0
https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/
"""
class Solution:
	"""
	Make temporary list recording last occuring 1s in each row.
	Now first row in grid can have 1 at maximum 0 index, nothing more.
	Second row can have 1 at maximum 1 index, and so on.
	Sort by swapping using greedy method, and return -1 if the above
	condition is not fulfilled at any point.
	# NOTE: IMPORTANT. Good question.
	"""
	def minSwaps(self, grid):
		temp = [0 for x in grid]
		for i in range(len(grid)):
			for j in range(len(grid)-1, -1, -1):
				if grid[i][j] == 1:
					temp[i] = j
					break
		k = 0
		for i in range(len(temp)):
			if temp[i] > i:
				j = i
				while temp[j] > i:
					j += 1
					if j >= len(temp):
						return -1
				temp = temp[:i] + [temp[j]] + temp[i:j] + temp[j+1:]
				k += abs(i-j)
		return k

grid = [[1,0,0,0,0,0],[0,1,0,1,0,0],[1,0,0,0,0,0],[1,1,1,0,0,0],[1,1,0,1,0,0],[1,0,0,0,0,0]]
x = Solution()
print(x.minSwaps(grid))
