from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1 buld the freq map
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        #2 arrange buckets
        bucket = [[] for _ in range(len(nums) + 1)]

        for num, freq in freq_map.items():
            bucket[freq].append(num)

        #3 traverse the bucket
        res = []
        for freq in range(len(bucket)-1, -1,-1):
            for num in bucket[freq]:
                res.append(num)
                if len(res) == k:
                    return res

        return res

        