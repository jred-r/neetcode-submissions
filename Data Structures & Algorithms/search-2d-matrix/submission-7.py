class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for index, nums in enumerate(matrix):
            start, end = nums[0], nums[-1]
            if start <= target <= end:
                return self.binary_search(nums, target)
            elif target < start:
                break
            else:
                continue

        return False
        
    def binary_search(self, nums: List[int], target : int):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left= mid + 1
            else:
                right = mid - 1
        return False
        