"""
Odd Even Linked List
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
	"""
	Since it is a linked list, space complexity is not a problem here.
	We can maintain the start of odd and even lists and join them at
	end by keeping the pointer to the even list start.
	"""
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head:
            odd = head
            even = head.next
            he = even
            while even and even.next:
                odd.next = odd.next.next
                even.next = even.next.next
                odd = odd.next
                even = even.next
            odd.next = he
        return head

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)
a.next.next.next.next.next = ListNode(6)
a.next.next.next.next.next.next = ListNode(7)

x = Solution()
print(x.oddEvenList(a))
