"""
Rotting Oranges
In a given grid, each cell can have one of three values:
the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
# NOTE: IMPORTANT! GOOD QUESTION.
"""
class Node:
	def __init__(self, time_frame, coordinates):
		self.time_frame = time_frame
		self.coordinates = coordinates
		self.next = None

class Solution:
	"""
	Have to process all the '2' instance together, so we create a queue. More
	importantly, we create a data structure that can hold the time_frame as well
	as the current coordinates.
	"""
	def __init__(self):
		self.grid = None
	def orangesRotting(self, grid):
		self.grid = grid
		queue, fresh = self.get_initial_queue()
		max_time = 0
		while queue:
			current_time_frame = queue[0].time_frame
			current_x, current_y = queue[0].coordinates[0], queue[0].coordinates[1]
			queue.pop(0)
			neighbor = self.helper(current_x-1, current_y, current_time_frame)
			if neighbor != None:
				fresh -= 1
				queue.append(neighbor)
			neighbor = self.helper(current_x, current_y-1, current_time_frame)
			if neighbor != None:
				fresh -= 1
				queue.append(neighbor)
			neighbor = self.helper(current_x+1, current_y, current_time_frame)
			if neighbor != None:
				fresh -= 1
				queue.append(neighbor)
			neighbor = self.helper(current_x, current_y+1, current_time_frame)
			if neighbor != None:
				fresh -= 1
				queue.append(neighbor)
			max_time = max(max_time, max([x.time_frame for x in queue], default=0))
		for i in range(len(self.grid)):
			for j in range(len(self.grid[0])):
				if self.grid[i][j] == 1:
					return -1
		return max_time
	
	def get_initial_queue(self):
		queue = []
		fresh = 0
		for i in range(len(self.grid)):
			for j in range(len(self.grid[0])):
				if self.grid[i][j] == 1:
					fresh += 1
				if self.grid[i][j] == 2:
					temp = Node(0, (i, j))
					queue.append(temp)
		return queue, fresh
	
	def helper(self, x, y, time):
		if x < 0 or y < 0 or x >= len(self.grid) or y >= len(self.grid[0]) or self.grid[x][y] != 1:
			return None
		self.grid[x][y] = 2
		return Node(time_frame=time+1, coordinates=(x, y))


grid = [[2,1,1],
		[1,1,0],
		[0,1,1]]
x = Solution()
print(x.orangesRotting(grid))
