class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        fixed = 0
        n = len(nums)
        nums.sort()
        for fixed in range(n):
            if fixed >= 1 and nums[fixed - 1] == nums[fixed]:
                continue #skip duplicates on the fixed

            l = fixed +1 
            r = n - 1
            while l < r:
                total = nums[fixed] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[fixed], nums[l], nums[r]])
                   
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r-1]:
                        r-=1
                    
                    l+=1
                    r-=1
                elif total < 0:
                    l+=1
                else:
                    r-=1                   

        return res

        