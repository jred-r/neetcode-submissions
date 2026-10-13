# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        # we use two pointers, one pointer is at the start and the other one ends up at nth node
        for _ in range(n):
            fast = fast.next
        # if fast is none, return head
        if fast is None:
            return head.next
        # move the slow and fast till we reach the tail,
        # the fast is on the tail and the slow is at the element that we want to replace.
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head
