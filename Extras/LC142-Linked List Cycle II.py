"""
142. Linked List Cycle II
Medium
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.
Note: Do not modify the linked list.
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Follow-up:
Can you solve it without using extra space?
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	"""
	This is IMPORTANT.
	Classic question requires to detect the cycle. That is straight
	forward the hare and tortoise solution. But returning the node
	where the cycle started is tricky.
	Detect cycle as previously. Then wherever the fast and slow meet,
	do the following.
	Start the head and slow pointer and keep moving until they meet
	now. That is where the cycle started.
	# NOTE: This will work only if the loop starts with fast = slow = head.
	IMPORTANT NOTE: READ ABOVE.
	"""
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast and fast.next and slow:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return
        while head!=slow:
            head = head.next
            slow = slow.next
        return head

a = ListNode(3)
a.next = ListNode(2)
a.next.next = ListNode(0)
a.next.next.next = ListNode(-4)
a.next.next.next.next = a.next

x = Solution()
print(x.detectCycle(a))
