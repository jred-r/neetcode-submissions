class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we assing the nums into a set.
        num_set = set(nums)
        longest = 0
        #for each number in num_set, check if num-1 is in the set,
        #if it is, then it is already counted. else maintain a seq count.
        for num in num_set:
            if num-1 not in num_set:
                current_length = 0
                while num + current_length in num_set:
                    current_length += 1
                longest = max(longest, current_length)
        return longest            
        