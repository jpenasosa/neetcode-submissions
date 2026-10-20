import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            rock = heapq.heappop_max(stones) - heapq.heappop_max(stones)
            if rock:
                heapq.heappush_max(stones, rock)
            
        return stones[0] if stones else 0