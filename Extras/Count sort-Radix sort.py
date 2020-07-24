class Count:
	def count_sort(self, nums):
		rec = [[] for i in range(max(nums)+1)]
		print(rec)
		for i in nums:
			rec[i].append(i)
		out = []
		for i in rec:
			out.extend(i)
		return out

nums = [1,2,3,1,2,4,3,5,7,2]
x = Count()
print(x.count_sort(nums))
