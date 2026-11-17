class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        used = [False] * n

        def backtrack(curr_perm, used):
            if len(curr_perm) == n:
                result.append(curr_perm.copy())
                return

            for i in range(n):
                if not used[i]:
                    curr_perm.append(nums[i])
                    used[i] = True
                    backtrack(curr_perm, used)
                    curr_perm.pop()
                    used[i] = False

        backtrack([], used)
        return result
