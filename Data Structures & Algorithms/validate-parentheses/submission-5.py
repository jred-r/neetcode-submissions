class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = {"]":"[", ")":"(", "}":"{"}
        stack = []
        for ch in s:
            if ch not in parenthesis:
                stack.append(ch)
            else:
                if stack and ch in parenthesis and parenthesis[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False


        return not stack
        