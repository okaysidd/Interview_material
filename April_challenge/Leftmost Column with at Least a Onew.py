"""
Leftmost Column with at Least a One
(This problem is an interactive problem.)
A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.
Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.
You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:
BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [m, n], which means the matrix is m * n.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.
For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.

Example 1:
Input: mat = [[0,0],[1,1]]
Output: 0

Example 2:
Input: mat = [[0,0],[0,1]]
Output: 1

Example 3:
Input: mat = [[0,0],[0,0]]
Output: -1

Example 4:
Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 100
mat[i][j] is either 0 or 1.
mat[i] is sorted in a non-decreasing way.
"""
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix(object):
    def __init__(self, mat):
        self.mat = mat
    def get(self, x, y):
        return self.mat[x][y]
    def dimensions(self):
        return len(self.mat), len(self.mat[0])

class Solution:
	"""
	Solution 1: Do Binary search on each of the row and find value of left
				most occurrence of 1 in that row. Among the rows, one with
				left most occurrence of 1 will be the answer.
	Solution 2: (PS. It is brilliant) Starting from top right corner, start
				a pointer that can only towards left and down. If the current
				cell is 1, move left, otherwise move down. Keep updating the
				last seen occurrence of 1. That is the answer.
	"""
    def leftMostColumnWithOne(self, binaryMatrix):
        dim = binaryMatrix.dimensions()
        i = 0
        j = dim[1] - 1
        last = -1
        while i < dim[0] and j > -1:
            current = binaryMatrix.get(i, j)
            if current == 1:
                last = j
                j -= 1
            else:
                i += 1
        return last
        return -1

mat = [[0,0,0,0,1,1],
       [0,0,0,1,1,1],
       [0,0,0,0,1,1],
       [0,0,0,0,1,1],
       [0,0,0,1,1,1],
       [0,0,0,1,1,1]]
bm = BinaryMatrix(mat)
a = Solution()
print(a.leftMostColumnWithOne(bm))
