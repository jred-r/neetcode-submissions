class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        stack = []
        para = {"}": "{", ")": "(", "]": "["}

        for ch in s:
            if ch not in para:
                stack.append(ch)
            else:
                if stack and stack[-1] == para[ch]:
                    stack.pop()
                else:
                    return False

        return not stack
