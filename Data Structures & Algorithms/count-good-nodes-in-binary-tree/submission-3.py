# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None), get_overloads:
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if node is None: return 0
            max_val = max(max_val, node.val)
            good_nodes = 1 if node.val >= max_val else 0
            good_nodes += dfs(node.left, max_val)
            good_nodes += dfs(node.right, max_val)
            return good_nodes
        
        return dfs(root, root.val)
        