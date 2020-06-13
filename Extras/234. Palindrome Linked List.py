"""
234. Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true
"""
# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
		
class Solution:
	"""
	O(n) time and O(1) space solution that distorts the input list.
	"""
	def isPalindrome(self, head: ListNode) -> bool:
		slow = fast = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		slow = self.reversed(slow)
		fast = head
		while slow:
			if slow.val != fast.val:
				return False
			slow = slow.next
			fast = fast.next
		return True
	def reversed(self, head):
		prev = None
		current = head
		while current:
			temp = current.next
			current.next = prev
			prev = current
			current = temp
		return prev

class Solution2:
	"""
	O(n) time and O(n) space solution that does not distort the input list.
	"""
	def isPalindrome(self, head: ListNode) -> bool:
		s = []
		while head:
			s.append(head.val)
			head = head.next
		return s == s[::-1]

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(1)
a.next.next.next = ListNode(2)
a.next.next.next.next = ListNode(1)

x = Solution()
print(x.isPalindrome(a))
