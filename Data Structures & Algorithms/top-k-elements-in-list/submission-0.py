import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        heap = [(-count, num) for num, count in counts.items()]
        heapq.heapify(heap)

        result = []
        for _ in range(k):
            _, num = heapq.heappop(heap)
            result.append(num)

        return result
