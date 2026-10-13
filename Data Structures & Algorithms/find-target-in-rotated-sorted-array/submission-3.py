class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.pivot(nums)
        n = len(nums)

        if pivot == 0:
            return self.binary_search(nums, target, 0, n - 1)

        # If target is in the left sorted half
        if nums[0] <= target <= nums[pivot - 1]:
            return self.binary_search(nums, target, 0, pivot - 1)

        # Otherwise target is in the right sorted half
        return self.binary_search(nums, target, pivot, n - 1)
    

    def pivot(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return left


    def binary_search(self, nums, target, left, right):
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1
