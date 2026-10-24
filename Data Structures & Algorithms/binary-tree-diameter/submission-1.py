# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [root]
        info = {None: (0, 0)}  # (height, diameter)

        while stack:
            node = stack[-1]

            if node.left and node.left not in info:
                stack.append(node.left)
            elif node.right and node.right not in info:
                stack.append(node.right)
            else:
                node = stack.pop()

                lh, ld = info[node.left]
                rh, rd = info[node.right]

                info[node] = (
                    1 + max(lh, rh),
                    max(lh + rh, ld, rd),
                )

        return info[root][1]
