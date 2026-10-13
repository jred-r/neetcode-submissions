class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #base case
        listSize =  len(nums)
        if(listSize ==0 or listSize == 1):
            return False
        #create a list to store the items
        seen : List[int][listSize] = []

        #iterate over the list
        for num in nums:
            #return true in case the num is already seen
            if num in seen:
                return True
            else:
                seen.append(num)

        #fall thorough, no duplicates
        return False        