# At each number:

# 1. Take it
# 2. Explore
# 3. Undo taking it
# 4. Skip it
# 5. Explore

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current_subset = []

        def backtrack(index):
            if index == len(nums):
                result.append(current_subset.copy())
                return
            
            current_num = nums[index]

            # include the number
            current_subset.append(current_num)
            backtrack(index+1)

            #undo
            current_subset.pop()
            
            #Exclude
            backtrack(index+1)
        backtrack(0)
        return result

        