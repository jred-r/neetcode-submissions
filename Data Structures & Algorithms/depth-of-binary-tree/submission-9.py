# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        max_height = 0
        stack = [(root, 1)]
        while stack:
            node, height = stack.pop()
            max_height = max(height, max_height)
            if node.left:
                stack.append((node.left, height + 1))
            if node.right:
                stack.append((node.right, height + 1))
        return max_height
