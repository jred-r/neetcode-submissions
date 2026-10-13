class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k <=0:
            return []
        freq = defaultdict(int)
        for num in nums:
           freq[num] += 1

        sor = sorted(freq.items(), key=lambda x : x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(sor[i][0])

        return res
        