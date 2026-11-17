class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        n = len(candidates)

        def backtrack(index, current, total):
            if total == target:
                result.append(current.copy())
                return

            if index >= n or total > target:
                return
                
            current_num = candidates[index]
            current.append(current_num)
            backtrack(index + 1, current, total + current_num)
            current.pop()
            
            while index + 1 < n and candidates[index] == candidates[index + 1]:
                index += 1
            
            backtrack(index + 1, current, total)

        backtrack(0, [], 0)
        return result
