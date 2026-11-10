import heapq

class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.maxheap, num)

        if len(self.maxheap) > 1 and len(self.maxheap) >= len(self.minheap):
            num = heapq.heappop_max(self.maxheap)
            heapq.heappush(self.minheap, num)
        
        if len(self.minheap) > len(self.maxheap):
            num = heapq.heappop(self.minheap)
            heapq.heappush_max(self.maxheap, num)

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return self.maxheap[0]

        return (self.minheap[0] + self.maxheap[0])/2
