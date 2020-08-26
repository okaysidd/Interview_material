"""
Non-overlapping Intervals
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

Example 2:
Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.

Example 3:
Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
Note:
You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
"""
class Solution:
	"""
	Good question.
	Sort by starting points, and if two overlap, remove one with larger ending
	point, since we have to remove minimum.
	"""
	def eraseOverlapIntervals(self, intervals):
		intervals.sort(key=lambda x:x[0])
		i = 0
		res = 0
		while i < len(intervals)-1:
			if intervals[i][1] > intervals[i+1][0]:
				res += 1
				if intervals[i][1] > intervals[i+1][1]:
					intervals.pop(i)
				else:
					intervals.pop(i+1)
			else:
				i += 1
		return res

intervals = [[1,2],[2,3],[3,4],[1,3]]
x = Solution()
print(x.eraseOverlapIntervals(intervals))
