class BinarySearchRecursive:
	def search(self, items, k):
		print(items)
		l, r = 0, len(items)-1
		if l == r:
			print('l = r')
			print(items[l], k)
			if items[l] == k:
				return l
			else:
				return False
		else:
			mid = l + (r - l) // 2
			if items[mid] == k:
				return mid
			elif k > items[mid]:
				result = self.search(items[mid+1:], k)
				if result == False:
					return False
				else:
					return mid + result + 1
			else:
				result = self.search(items[:mid], k)
				if result == False:
					return False
				else:
					return result
		return False

items = [2,3,5,6,6,8,10,11,11,11,13,16]
k = 16
x = BinarySearchRecursive()
x.search(items, k)
