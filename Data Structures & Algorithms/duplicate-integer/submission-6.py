class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        Duplicates can be identified by iterating the 
        array on each element and comparing if there element has
        been seen more than once.
        This is a brute force approach and will resut in a runtime of O(n^2)

        An efficient way is to use a data structure which has a fast look up,
        iterate through each element in the array.
        check if the element exists, if it does then exit and indicate duplicate integer.
        
        We can use a set() for this, The look up is O(1). 
        we will need to iterate at most 'n' times resulting in o(n).
        
        '''

        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

        return False

        
        