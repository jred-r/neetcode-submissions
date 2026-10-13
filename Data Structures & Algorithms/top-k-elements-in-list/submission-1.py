class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort O(n)
        count = {}
        #create an array of arrays of length of input array
        freq = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            count[num] =  count.get(num, 0) + 1
        
        #assign count and keys to the freq array
        for num, cnt in  count.items():
            freq[cnt].append(num)
        
        res= []
        #iterate the array in reverse order and keep on appending values to the res[] till the desired length 'k' is reached
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if(len(res) == k):
                    return res