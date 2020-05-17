"""
Number of Islands
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3
"""
class Solution:
    """
    At every cell in the grid, if there is a '1', find all attached 1s
    and flip them to zero and update count by one. Those flipped won't
    be counted again and those not in touch with the previous island will
    not be flipped.
    """
    def numIslands(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and not(i > 0 and grid[i-1][j] == '1') and not(j > 0 and grid[i][j-1] == '1'):
                    self.callBFS(grid, i, j)
                    count += 1
        return count
    def callBFS(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0' or grid[i][j] == '-':
            return
        grid[i][j] = '-'
        self.callBFS(grid, i-1, j) # up
        self.callBFS(grid, i+1, j) # down
        self.callBFS(grid, i, j-1) # left
        self.callBFS(grid, i, j+1) # right

grid = [
    ['1','1','0','0','0'],
    ['1','1','0','0','0'],
    ['0','0','1','0','0'],
    ['0','0','0','1','1']
]
grid = [
    ['1', '0', '1', '0', '0'],
    ['0', '0', '1', '1', '1'],
    ['1', '0', '1', '1', '1'],
    ['1', '0', '0', '1', '0']
]
a = Solution()
print(a.numIslands(grid))
