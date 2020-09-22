"""
Image Overlap
Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)
We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.
(Note also that a translation does not include any kind of rotation.)
What is the largest possible overlap?

Example 1:
Input: A = [[1,1,0],
			[0,1,0],
			[0,1,0]]
	   B = [[0,0,0],
			[0,1,1],
			[0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
Notes: 
1 <= A.length = A[0].length = B.length = B[0].length <= 30
0 <= A[i][j], B[i][j] <= 1
# IMPORTANT QUESTION!
"""
from scipy.ndimage import convolve
import numpy as np

class Solution:
	"""
	Numpy solution for image convolution.
	"""
	def largestOverlap(self, A, B):
		B = np.pad(B, len(A), mode='constant', constant_values=(0, 0))
		return np.amax(convolve(B, np.flip(np.flip(A,1),0), mode='constant'))


class Solution2:
	"""
	Try all overlapping possibilities.
	"""
	def largestOverlap(self, A, B):
		N = len(A)
		best = 0
		for dx, dy in [(1,1), (1,-1), (-1,1), (-1,-1)]:
			for shiftx in range(N):
				for shifty in range(N):
					count = 0
					for x in range(N):
						for y in range(N):
							if A[x][y] == 1:
								nx, ny = x + dx * shiftx, y + dy * shifty
								if 0 <= nx < N and 0 <= ny < N and B[nx][ny] == 1:
									count += 1
					best = max(best, count)
		return best

A = [[1,1,0],
	[0,1,0],
	[0,1,0]]
B = [[0,0,0],
	[0,1,1],
	[0,0,1]]
x = Solution()
print(x.largestOverlap(A, B))
