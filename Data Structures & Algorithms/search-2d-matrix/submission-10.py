class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_search(nums: List[int]):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        for nums in matrix:
            if nums[0] <= target <= nums[-1]:
                return binary_search(nums)
            elif nums[0] > target:
                return False
        return False

        