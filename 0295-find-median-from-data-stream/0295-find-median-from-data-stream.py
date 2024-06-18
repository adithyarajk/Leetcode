class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if len(self.minheap) == len(self.maxheap):
            heappush(self.maxheap, -heappushpop(self.minheap, -num))
            heappush(self.minheap, -heappushpop(self.maxheap, num))


    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return float(self.maxheap[0] - self.minheap[0])/2
        else:
            return self.maxheap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()