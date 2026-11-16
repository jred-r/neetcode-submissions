class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(index, current, total):
            if total == target:
                result.append(current.copy())
                return
            
            if total > target or index >= len(nums):
                return
            
            current.append(nums[index])
            backtrack(index, current, total + nums[index])
            current.pop()
            backtrack(index+1, current, total)

        backtrack(0, [], 0)
        return result
        