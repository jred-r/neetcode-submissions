class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = nums
        for i in range(n):
            res.append(nums[i])
        return res
        