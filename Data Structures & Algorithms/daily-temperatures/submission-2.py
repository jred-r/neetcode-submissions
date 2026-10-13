class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for day,temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                s_day, s_temp = stack.pop()
                res[s_day] = day - s_day
            stack.append((day, temp))
        return res
        