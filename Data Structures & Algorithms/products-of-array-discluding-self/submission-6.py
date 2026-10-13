class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        total_product = 1
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total_product *= num

        if zero_count > 1:
            return [0 for _ in range(len(nums))]
        
        res = []
        for num in nums:
            if zero_count == 1:
                if num == 0:
                    res.append(total_product)
                else:
                    res.append(0)
            else:
                res.append(total_product // num)
        return res
            


        