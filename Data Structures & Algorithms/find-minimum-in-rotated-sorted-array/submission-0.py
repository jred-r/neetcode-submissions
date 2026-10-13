class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_value = nums[0]
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] < nums[right]:
                return min(min_value, nums[left])
                
            mid = left + (right - left) // 2
            min_value = min(min_value, nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid -1 
        
        return min_value
            



        