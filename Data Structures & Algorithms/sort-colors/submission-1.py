class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        moving = 0
        fixed = 0

        def swapItems(number: int):
            nonlocal moving, fixed
            while moving < n:
                while moving < n and nums[moving] != number:
                    moving += 1
                if moving < n:
                    nums[moving], nums[fixed] = nums[fixed], nums[moving]
                    moving += 1
                    fixed += 1

        swapItems(0)
        moving = fixed
        swapItems(1)
        moving = fixed
        swapItems(2)
