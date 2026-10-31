class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create the dict with num and count
        num_counts = defaultdict(int)
        for num in nums:
            num_counts[num] += 1
        
        #create the buckets
        buckets = [[] for _ in range(len(nums) + 1)]

        #assign values in the buckets
        for num, count in num_counts.items():
            buckets[count].append(num)

        res = []
        #iterate the buckets from the end and return 'k' values
        for bucket in range(len(buckets)-1, -1, -1):
            for num in buckets[bucket]:
                res.append(num)
                if len(res) == k:
                    return res
        return res

        

        