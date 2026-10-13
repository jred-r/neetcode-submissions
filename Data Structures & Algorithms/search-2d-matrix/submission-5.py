class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            low, high = row[0], row[-1]
            if low <= target <= high:
                return self.binarySearch(row, target)
            elif target < low:
                return False
            else:
                continue
        return False

    def binarySearch(self, nums : List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
