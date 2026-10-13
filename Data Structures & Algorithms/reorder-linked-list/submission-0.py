# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        # find the middle of the list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half of the list,
        # it starts from slow.next
        second = slow.next
        prev = None
        slow.next = None
        # slow.next becomes the end of the reordered list
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next

        first = head
        second = prev
        # swap the nodes
        while second:
            f_node, s_node = first.next, second.next
            first.next = second
            second.next = f_node
            first, second = f_node, s_node
