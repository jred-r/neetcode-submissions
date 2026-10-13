class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch == "+":
                stack.append(stack.pop() + stack.pop())
            elif ch == "-":
                n1, n2 = stack.pop(), stack.pop()
                stack.append(n2-n1)
            elif ch == '*':
                stack.append(stack.pop() * stack.pop())
            elif ch == "/":
                n1,n2 = stack.pop(), stack.pop()
                stack.append(int(float(n2) / n1))
            else:
                stack.append(int(ch))
        
        return stack.pop()


            
        