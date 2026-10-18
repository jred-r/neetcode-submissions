# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            # assign temp next node
            next_node = current.next
            # flip the pointer direction to prev
            current.next = prev
            # now nove prev by one postion
            prev = current
            # move current by one position
            current = next_node
        return prev
        #return the prev as current would have moved on to the end of the List and is None
