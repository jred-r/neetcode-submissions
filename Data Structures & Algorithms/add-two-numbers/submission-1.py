# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = result =  ListNode()
        carry = 0
        while l1 or l2 or carry:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            n3 = n1 + n2 + carry
            digit = n3 % 10
            carry = n3 // 10
            result.next = ListNode(digit)
            result = result.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next

        