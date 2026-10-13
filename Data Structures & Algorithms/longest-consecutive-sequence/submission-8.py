class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums_set:
            if num-1 not in nums_set:
                current_longest = 1
                while num + current_longest in nums_set:
                    current_longest += 1
                longest = max(longest, current_longest)
        return longest

        