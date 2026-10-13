class Solution:
    def isValid(self, s: str) -> bool:
        para = {"}": "{", "]": "[", ")": "("}
        stack = []
        for c in s:
            if c in para:
                if stack and stack[-1] == para[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        return not stack
        



    
