"""
Task Scheduler
You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter represents a different task. Tasks could be done without the original order of the array. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
You need to return the least number of units of times that the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Example 3:
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

Constraints:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""
class Solution:
	"""
	One of two things will decide the solution:
	1. Either the most frequent has enough occurences to adjust all less frequent
		ones in the n spaces between them.
	2. Less frequent are abundant and length of the tasks in itself is enough to
		store everything.
	"""
	def leastInterval(self, tasks, n):
		d = {}
		for t in tasks:
			if t in d:
				d[t] += 1
			else:
				d[t] = 1
		d_ = list(d.items())

		d_.sort(key = lambda x:x[1], reverse=True)
		
		# result = (d_[0][1] - 1) * (n + 1)
		result = (1+n)*d_[0][1] - n # for max frequency

		for x, y in d_[1:]:
			if y == d_[0][1]:
				result += 1
			else:
				break
		return max(result, len(tasks))

class Solution2:
	"""
	Gives time limit exceeded.
	Using heap should solve that problem.
	"""
	def leastInterval(self, tasks, n):
		d = {}
		for t in tasks:
			if t in d:
				d[t] += 1
			else:
				d[t] = 1
		current_window = []
		res = 0
		d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
		d_ = list([[x[0], x[1]] for x in d.items()])
		while len(d_) > 0:
			if len(current_window) > n: current_window.pop(0)
			added = False
			for x in range(len(d_)):
				if d_[x][0] not in current_window:
					res += 1
					current_window.append(d_[x][0])
					d_[x][1] -= 1
					if d_[x][1] == 0:
						d_.pop(x)
					added = True
					while x < len(d_)-1 and d_[x][1] < d_[x+1][1]:
						d_[x], d_[x+1] = d_[x+1], d_[x]
						x += 1
					break
			if not added:
				current_window.append('idle')
				res += 1
		return res


tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
x = Solution()
print(x.leastInterval(tasks, n))
