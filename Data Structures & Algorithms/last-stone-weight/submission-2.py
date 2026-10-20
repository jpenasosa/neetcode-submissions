import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop_max(stones)
            stone2 = heapq.heappop_max(stones)
            if (rock := stone1 - stone2) > 0:
                heapq.heappush_max(stones, rock)
            
        return stones[0] if stones else 0