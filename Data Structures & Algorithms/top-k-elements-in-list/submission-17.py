class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1
        #create empty buckets
        buckets = [[] for _ in range(len(nums) + 1)]
        #fill in the buckets
        for num, freq in freq_map.items():
            buckets[freq].append(num)

        res = []

        for freq in range(len(buckets)-1, -1, -1):
            bucket = buckets[freq]
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res

        return res

        