class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        response = [0] * len(temperatures)
        stack = [] #storing (temp, day)
        for day, temp in enumerate(temperatures):
            while stack and temp >stack[-1][0]:
                stack_temp, stack_day = stack.pop()
                response[stack_day] = day - stack_day
            stack.append((temp, day))
        return response
        