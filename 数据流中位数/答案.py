import heapq


class MedianFinder:

    def __init__(self):
        self.len = 0
        self.Max_heap = []
        self.Min_heap = []
    def addNum(self, num):
        self.len+=1
        heapq.heappush(self.Max_heap,(-num,num))
        _,max_heap_top = heapq.heappop(self.Max_heap)
        heapq.heappush(self.Min_heap,max_heap_top)
        if self.len & 1:
            min_heap_top = heapq.heappop(self.Min_heap)
            heapq.heappush(self.Max_heap,(-min_heap_top,min_heap_top))
    def findMedian(self):
        if self.len == 0:
            return None
        if self.len%2:
            return self.Max_heap[0][1]
        else:
            return (self.Max_heap[0][1]+self.Min_heap[0])/2
s = MedianFinder()
print(s.findMedian())
s.addNum(1)
print(s.findMedian())
s.addNum(2)
print(s.findMedian())
s.addNum(0)
print(s.findMedian())
