from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)

        for r in range(rows):
            first = matrix[r][0]
            last = matrix[r][-1]

            if target < first:
                return self.binary_search(matrix[r - 1], target) if r > 0 else False

            if first <= target <= last:
                return self.binary_search(matrix[r], target)

        return False

    def binary_search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return True
        return False
