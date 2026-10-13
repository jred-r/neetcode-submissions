class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:  
        nums.sort()
        n = len(nums)
        scan = 0
        res = []
        for scan in range(n):
            #skip the duplicate scan location
            if scan >= 1 and nums[scan] == nums[scan-1]:
                continue
            
            left = scan + 1
            right = n - 1
            #we use the standard 2 pointer approach here
            while left < right:
                total = nums[scan] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[scan], nums[left], nums[right]])
                    #skip duplicate left
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    while left< right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -=1
            
        return res

        