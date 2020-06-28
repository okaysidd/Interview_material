"""
Heaps are used when the highest or lowest order/priority element needs to be
removed. They allow quick access to this item in O(1) time. One use of a
heap is to implement a priority queue.
Binary heaps are usually implemented using arrays, which save overhead cost
of storing pointers to child nodes.
Cons of Using Heaps
Heaps only provide easy access to the smallest/greatest item. Finding other
items in the heap takes O(n) time because the heap is not ordered. We must
iterate through all the nodes.
# NOTE: IMPORTANT
If we are looking at the i-th index in an array:
	It’s parent is at the floor (i-1)/2 index.
	It’s left child is at 2 * i + 1 index.
	It’s right child is at 2 *i + 2 index.
"""
class Heap:
	def __init__(self):
		self.heap = []
	def add(self, val):
		n = len(self.heap)
		self.heap.append(val)
		while n >= 0 and self.heap[(n-1)//2] > self.heap[n]:
			self.heap[(n-1)//2], self.heap[n] = self.heap[n], self.heap[(n-1)//2]
			n = (n-1)//2
		return self.heap
	def delete(self):
		top = self.heap[0]
		self.heap[0] = self.heap[-1]
		self.heap.pop()
		n = 0
		while (n*2)+2 <= len(self.heap):
			if self.heap[n] > self.heap[(n*2)+1] or self.heap[n] > self.heap[(n*2)+2]:
				if self.heap[(n*2)+1] < self.heap[(n*2)+2]:
					self.heap[n], self.heap[(n*2)+1] = self.heap[(n*2)+1], self.heap[n]
					n = (n*2)+1
				else:
					self.heap[n], self.heap[(n*2)+2] = self.heap[(n*2)+2], self.heap[n]
					n = (n*2)+2
		return top

a = Heap()
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(5)
a.add(2)
a.add(2)
a.add(2)
a.add(2)
print(a)

a.delete()
print(a)