class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_search(nums: List[int]):
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

        for nums in matrix:
            start, end = nums[0], nums[-1]
            if start <= target <= end:
                return binary_search(nums)
            elif target < start:
                break
            else:
                continue

        return False
        
    
        