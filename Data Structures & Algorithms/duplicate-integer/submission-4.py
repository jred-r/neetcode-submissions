class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        "Time complexity here has been reduced to O(n) as we are using a set"
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

        