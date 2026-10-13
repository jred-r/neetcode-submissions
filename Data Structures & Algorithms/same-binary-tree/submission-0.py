# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p, q)])
        while queue:
            node_p, node_q = queue.popleft()

            # check if both nodes are empty
            if node_p is None and node_q is None:
                continue
            # check if either of the nodes are empty
            # or if values are not equal
            if node_p is None or node_q is None:
                return False

            if node_p.val != node_q.val:
                return False

            # queue the left and right nodes
            queue.append((node_p.left, node_q.left))
            queue.append((node_p.right, node_q.right))

        return True
