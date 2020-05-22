"""
206. Reverse Linked List
Reverse a singly linked list.
Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
class Solution:
	"""
	Iterative. Create dummy previous node and then at every step
	assign .next of current head to its prev, then slide both of
	them ahead.
	"""
	def reverseList(self, head):
		prev = ListNode(None)
		while head:
			temp = head.next
			head.next = prev
			prev = head
			head = temp
		self.display(prev)
		return prev
	def display(self, head):
		while head:
			print(f'{head.val} -> ', end='')
			head = head.next
		print()

class Solution2:
	"""
	Iterative. Create a new dummy node and replace its head everytime
	with the head of old list, thus effectively pushing them down.
	Like a stack made linked list.
	"""
	def reverseList(self, head: ListNode) -> ListNode:
		new = ListNode(0)
		while head:
			temp = head.next
			temp2 = new.next
			new.next = head
			new.next.next = temp2
			head = temp
		return new.next

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)
x = Solution()
print(x.display(a))
print(x.reverseList(a))
