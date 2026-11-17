class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        n = len(nums)
        def backtrack(index):
            if index >= n:
                result.append(subset.copy())
                return
            
            subset.append(nums[index])
            backtrack(index+1)
            subset.pop()
            backtrack(index+1)
            
        backtrack(0)
        return result

        