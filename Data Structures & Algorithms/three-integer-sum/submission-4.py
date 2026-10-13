class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for fixed in range(n):
             #skip duplicate fixed
            if fixed > 0 and nums[fixed] == nums[fixed - 1]:
                continue

            left = fixed + 1
            right = n - 1

            while left < right:
               
                sum = nums[fixed] + nums[left] + nums[right]
                if sum == 0:
                    res.append([nums[fixed], nums[left], nums[right]])  
                    #skip duplicate left
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    #skip duplicate right
                    while left < right and nums[right] == nums[right -1]:
                        right -= 1
                    #increment left and decrement right
                    left += 1
                    right -= 1

                elif sum < 0:
                    left += 1
                else:
                    right -= 1
            
        return res
                        
        