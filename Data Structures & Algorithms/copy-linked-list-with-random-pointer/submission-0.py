"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current_list = {None:None}
        current = head
        while current:
            copy = Node(current.val)
            current_list[current] = copy
            current = current.next
        
        current = head
        while current:
            new_node = current_list[current]
            new_node.next = current_list[current.next]
            new_node.random = current_list[current.random]
            current = current.next
        return current_list[head]
        