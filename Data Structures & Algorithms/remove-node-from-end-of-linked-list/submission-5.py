# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #assign a new dummy node, which points to the head
        dummy = ListNode(0, head)
        left, right = dummy, head
        #move the right by n-positions, thus creating an offset
        while n > 0:
            right = right.next
            n -= 1
        #now move, left and right till we reach the tail, 
        #left is exactly 1 element before the node that needs to be removed
        while right:
            left = left.next
            right = right.next
        #set left so that it skips the element
        left.next = left.next.next
        #return head
        return dummy.next
        
        

       


        