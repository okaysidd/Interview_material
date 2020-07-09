"""
160. Intersection of Two Linked Lists
Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:
1-2-3-4-5
   /
6-7
begin to intersect at node 3.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

Example 2:
Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	"""
	Finding intersection is easy. Traverse both and if their
	end nodes are same, they intersected somewhere. Tricky part
	is to find the point of intersection.
	Two solutions for that basically.
	1) Traverse both and store their lengths. Then traverse both
	together, ensuring longer one catches up with the smaller one
	and then traverse both together, whereever they match, that's
	the intersection, whether a node or None.
	2) Traverse both and unless both become equal (node or None),
	replace one node with head of another if it reaches the end.
	IT WORKS.
	"""
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return
        a = headA
        b = headB
        while a != b:
            if a == None:
                a = headB
            else:
                a = a.next
            if b == None:
                b = headA
            else:
                b = b.next
        return a

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
b = ListNode(5)
b.next = ListNode(6)
b.next.next = a.next.next

x = Solution()
print(x.getIntersectionNode(a, b))
