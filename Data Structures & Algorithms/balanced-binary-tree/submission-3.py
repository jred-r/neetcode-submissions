# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def dfs(node):
            nonlocal balanced
            if not node or not balanced:
                return 0
            
            lh = dfs(node.left)
            rh = dfs(node.right)
            if balanced and abs(lh - rh) > 1:
                balanced = False
            height = 1 + max(lh, rh)
            return height
        
        dfs(root)
        return balanced
        