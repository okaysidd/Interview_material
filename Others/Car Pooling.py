"""
Car Pooling
You are driving a vehicle that has capacity empty seats initially available for passengers.  The vehicle only drives east (ie. it cannot turn around and drive west.)
Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains information about the i-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off.  The locations are given as the number of kilometers due east from your vehicle's initial location.
Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

Example 1:
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

Example 2:
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true

Example 3:
Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true

Example 4:
Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true

Constraints:
trips.length <= 1000
trips[i].length == 3
1 <= trips[i][0] <= 100
0 <= trips[i][1] < trips[i][2] <= 1000
1 <= capacity <= 100000
"""
class Solution:
	"""
	Mapping out all the trips on a timeline.
	"""
	def carPooling(self, trips, capacity):
		max_loc = max([x[2] for x in trips])
		dp = [0] * (max_loc+1)
		for trip in trips:
			for j in range(trip[1], trip[2]):
				dp[j] += trip[0]
				# print(dp)
				if dp[j] > capacity:
					return False
		return True

class Solution2:
	"""
	Instead of mapping out all the trips on a timeline, mapping only the starting and ending
	points of the trip and accumalating at the last.
	To map only starting and ending points, map the start point as +number of passengers,
	and the end as -number of passengers. Pretty clever. # NOTE: IMPORTANT. GOOD SOLUTION.
	"""
	def carPooling(self, trips, capacity):
		max_loc = max([x[2] for x in trips])
		dp = [0] * (max_loc+1)
		for trip in trips:
			dp[trip[1]] += trip[0]
			dp[trip[2]] -= trip[0]
		for i in range(1, len(dp)):
			dp[i] += dp[i-1]
		return max(dp) <= capacity

trips = [[3,2,7],[3,7,9],[8,3,9]]
capacity = 11
x = Solution2()
print(x.carPooling(trips, capacity))
