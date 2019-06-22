class MedianFinder:

    def __init__(self):
        self.ls = []
    def addNum(self, num):
        self.ls.append(num)
    def findMedian(self):
        l = len(self.ls)
        if l == 0:
            return None
        if l%2:
            return self.ls[int(l/2)]
        else:
            return (self.ls[int(l/2)-1]+self.ls[int(l/2)])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

s = MedianFinder()
# s.addNum(1)
# s.addNum(2)
# s.addNum(2)
x = s.findMedian()
print(x)