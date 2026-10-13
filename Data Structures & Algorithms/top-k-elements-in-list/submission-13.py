class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create the freq map, #create buckets, return the valules from the bucket in reverse order.
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for key, value in freq_map.items():
            buckets[value].append(key)
        
        res = []
        for index in range(len(buckets)-1, 0, -1):
            for num in buckets[index]:
                res.append(num)
                if len(res) == k:
                    return res

        return []        
        