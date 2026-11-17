import heapq

class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.maxHeap, num)

        if len(self.maxHeap) > len(self.minHeap):
            num = heapq.heappop_max(self.maxHeap)
            heapq.heappush(self.minHeap, num)
        
        if len(self.minHeap) > len(self.maxHeap):
            num = heapq.heappop(self.minHeap)
            heapq.heappush_max(self.maxHeap, num)


    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0]
        
        return (self.maxHeap[0] + self.minHeap[0])/2
        
        