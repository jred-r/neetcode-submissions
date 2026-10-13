class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        resp = defaultdict(int)
        for num in nums:
            resp[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for key, value in resp.items():
            buckets[value].append(key)
        
        ret = []
        for index in range(len(buckets)-1, -1, -1):
            for value in buckets[index]:
                ret.append(value)
                if len(ret) == k:
                    return ret

        return ret


        