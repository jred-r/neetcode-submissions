class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        num_product = 1
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                num_product *= num
            if zero_count > 1:
                return [0] * len(nums)
        
        response = []
        for num in nums:
            if zero_count == 1:
                if num == 0:
                    response.append(num_product)
                else:
                    response.append(0)
            else:
                response.append(num_product // num)
        return response
        