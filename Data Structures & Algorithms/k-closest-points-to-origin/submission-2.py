import heapq

class Solution:
    def squareDistance(self, point: List[int]) -> int:
        x, y = point
        return x*x + y*y

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist2 = self.squareDistance(point)
            heapq.heappush(heap, (dist2, point))
        
        return [pt for _, pt in heapq.nsmallest(k, heap)]
