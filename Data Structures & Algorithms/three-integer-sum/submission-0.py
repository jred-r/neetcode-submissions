class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums) - 1
        fixed = 0
        while fixed < n:
            # skip the duplicate fixed number.
            if fixed > 0 and nums[fixed - 1] == nums[fixed]:
                fixed += 1
                continue

            l = fixed + 1
            r = n

            while l < r:
                curr = nums[fixed] + nums[l] + nums[r]
                if curr == 0:
                    res.append([nums[fixed], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1

                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1

                elif curr < 0:
                    l += 1
                else:
                    r -= 1
            fixed += 1

        return res

        