"""
Minimum Path Sum
Solution
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""
class Solution:
	"""
	At every cell starting from the top left corner (except the extreme
	top left corner), assign the cell with minimum of the cell on left
	of it or above it, hence emulating the movement to only right and
	down. Doing this for the complete grid will give the final answer
	at the bottom right corner.
	"""
    def minPathSum(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0 and j == 0:
                    continue
                if i-1 < 0:
                    grid[i][j] += grid[i][j-1]
                elif j-1 < 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[len(grid)-1][len(grid[0])-1]

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
a = Solution()
print(a.minPathSum(grid))
