# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSame(root, subroot) -> bool:
            queue = deque([(root, subroot)])
            while queue:
                t1, t2 = queue.popleft()
                if t1 is None and t2 is None:
                    continue
                
                if t1 is None or t2 is None:
                    return False
                
                if t1 and t2 and t1.val != t2.val:
                    return False
                
                queue.append((t1.left, t2.left))
                queue.append((t1.right, t2.right))
            return True
        
        root_stack = [root]
        while root_stack:
            t1 = root_stack.pop()
            if t1.val == subRoot.val:
                same = isSame(t1, subRoot)
                if same: return True
            
            if t1.left: root_stack.append(t1.left)
            if t1.right: root_stack.append(t1.right)

        return False


        