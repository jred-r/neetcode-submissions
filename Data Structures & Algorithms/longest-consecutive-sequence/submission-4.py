class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        
        longest = 0
        nums_set = set(nums)
        for num in nums_set:
            if not num-1 in nums_set:#this is a new element that we have not seen:
                curr = 1
                while num +curr in nums_set: #we check if the next number is in the set
                    curr += 1
                longest = max(longest, curr)
        
        return longest

        