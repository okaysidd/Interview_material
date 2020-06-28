"""
Count Square Submatrices with All Ones
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:
Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
Constraints:
1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
"""
class Solution:
	"""
	Starting from top left cell in matrix, we will attempt to count all the
	sqaures by pointing to their bottom right corner. By moving through the
	matrix, it is to be noted that a cell is only as strong as its weakest
	neighbour (left, up and diagonal up-left). We get the min from these and
	add 1 for the current square. Every time we encounter a 1 in the first row
	or first column, we add one to the number of squares.
	We also add 1 to the result everytime we find a 1, because it is a sqaure
	on its own.
	"""
	def countSquares(self, matrix) -> int:
		res = 0
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				if matrix[i][j] == 1:
					if i == 0 or j == 0:
						res += 1
					else:
						matrix[i][j] = min(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j]) + 1 # because it is a sqaure on its own
						res += matrix[i][j]
		return res

matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
x = Solution()
print(x.countSquares(matrix))
