class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         #we can do this using prefix and postfix approach
        product = [1] * (len(nums))
        #calcuate the prefix product
        prefix = 1
        for i in range(len(nums)):
            product[i] = prefix
            prefix *= nums[i]
        
        #calucate the postfix and multiply with the prefix value
        postfix = 1
        for i in range(len(nums) -1,-1,-1):
            product[i] *= postfix
            postfix *= nums[i]
        
        return product