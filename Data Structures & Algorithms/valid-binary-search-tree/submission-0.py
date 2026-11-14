# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None: return False
        queue = deque([(root, -math.inf, math.inf)])
        while queue:
            node, max_left, max_right = queue.popleft()
            if max_left < node.val < max_right:
                if node.left: queue.append((node.left, max_left, node.val))
                if node.right: queue.append((node.right, node.val, max_right))
            else:
                return False

        return True
        