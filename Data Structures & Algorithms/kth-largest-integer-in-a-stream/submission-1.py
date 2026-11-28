class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        self.k = k
        self._pop()

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        self._pop()
        return self.minHeap[0]      

    def _pop(self):
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

