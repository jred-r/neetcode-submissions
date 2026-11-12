# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(p, q):
            queue = deque([(p, q)])
            while queue:
                n1, n2 = queue.popleft()

                if n1 is None and n2 is None:
                    continue

                if n1 is None or n2 is None:
                    return False

                if n1.val != n2.val:
                    return False

                queue.append((n1.left, n2.left))
                queue.append((n1.right, n2.right))

            return True

        stack = [root]

        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                same = isSame(node, subRoot)
                if same: return True
            
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        
        return False
            
