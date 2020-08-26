"""
Minimum Number of Arrows to Burst Balloons
There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.
An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Example:
Input:
[[10,16], [2,8], [1,6], [7,12]]
Output:
2
Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
"""
class Solution:
	"""
	Good question. If we sort by end points, and start with the first
	interval, if the start of the interval is larger than the current
	end, a new shot will be required, and now with this shot we can
	cover till the last of this interval, so we update the end as well.
	"""
	def findMinArrowShots(self, points):
		points.sort(key=lambda x:x[1])
		res = 0
		end = -99999999999999999999
		for i in points:
			if i[0] > end:
				res += 1
				end = i[1]
		return res

points = [[10,16], [2,8], [1,6], [7,12]]
x = Solution()
print(x.findMinArrowShots(points))
