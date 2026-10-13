class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """I need to verify if the list contains any two numbers that can add up to the target
        I can acheive this by looking at the current number and scanning the list to check if-
        there exists a number which, when added to it, results in the target number.
        this cab be achecived by looking for current + target-current
        for num in nums:"""
        """    
            if (target-num) in nums:
                indices = [nums.index(num), nums.index(target-num)]
                return indices
        """
        """the above code fails when the same number is encountered twice, like 5 + 5 = 10
        num_to_index is a hash map that stores the index of each number as you iterate through nums.
        For each number num, you calculate its complement as target - num.
        If the complement is found in num_to_index, it means that there is a previous number that,-
          -when added to the current number, gives the target. Therefore, you return the indices of both numbers.
        If the complement is not found, you store the current number and its index in the num_to_index hash map.
        """
        num_indices = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement],i]
            num_indices[num] = i

