"""
Unique Paths III
On a 2-dimensional grid, there are 4 types of squares:
1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Example 1:
Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 2:
Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:
Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.

Note:
1 <= grid.length * grid[0].length <= 20
# NOTE: IMPORTANT! GOOD QUESTION
"""
class Solution:
	"""
	1. Find starting spot, and number of cells that can be visited- 0, 1, 2 (1 is 
		where we start, 2 is the end, 0 are the empty cells).
	2. Start dfs from starting cell and traverse to all directions, marking the
		current cell to -2, to avoid visiting again and decrementing empty cells
		everytime.
	3. Once the recursion is complete, set the -2 back to its original cell value, for
		other recursion stacks.
	4. Check for bounds of the grid. If 2 is reached and number of unvisited empty cells
		is 0, increment result.
	"""
	def uniquePathsIII(self, grid):
					
		def dfs(x, y, rest):
			nonlocal result
			if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] < 0:
				return
			if grid[x][y] == 2 and rest == 0:
				result += 1
				
			neibs = [[0,1],[0,-1],[1,0],[-1,0]]
			for dx, dy in neibs:
				temp = grid[x][y]
				grid[x][y] = -2
				dfs(x+dx, y+dy, rest - 1)
				grid[x][y] = temp

		empty = 0
		result = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == 1:
					sx, sy = i, j
				if grid[i][j] != -1:
					empty += 1
					
		dfs(sx, sy, rest=empty-1)
		return result

grid = [[1,0,0,0],
        [0,0,0,0],
        [0,0,2,-1]]
x = Solution()
print(x.uniquePathsIII(grid))
