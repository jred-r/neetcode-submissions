# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #we use bfs and traverse level by level.
        #at each level, if we dont have the right node then we add the left node.
        if root is None:
            return []
        res = []
        queue = deque([root]) if root else deque()
        while queue:
            level_values = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level_values.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)        
            if level_values:
                res.append(level_values[-1])
        return res

        