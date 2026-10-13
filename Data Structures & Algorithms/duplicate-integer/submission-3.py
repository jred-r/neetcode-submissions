class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """simple implementation, create a simple list, 
            iterate over the given list and keep on adding items that you see,
            if you have already seen the number before, exit as you found the duplicate."""
        seen = []
        for num in nums:
            if num in seen:
                return True
            else:
                seen.append(num)
        return False
