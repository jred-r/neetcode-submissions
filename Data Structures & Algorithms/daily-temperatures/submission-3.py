class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for day, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_day = stack.pop()
                res[stack_day] = day - stack_day
            stack.append((temp, day))
        return res 

        