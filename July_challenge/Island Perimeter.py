"""
Island Perimeter
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.
Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:
Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
Output: 16
"""
class Solution:
	def islandPerimeter(self, grid):
		def helper(grid, i, j):
			if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0:
				return 1
			return 0
		temp = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == 1:
					temp += helper(grid, i-1, j)
					temp += helper(grid, i, j-1)
					temp += helper(grid, i+1, j)
					temp += helper(grid, i, j+1)
		return temp

grid = [[0,1,0,0],
		[1,1,1,0],
		[0,1,0,0],
		[1,1,0,0]]
x = Solution()
print(x.islandPerimeter(grid))
