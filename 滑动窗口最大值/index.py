class Que:
    def __init__(self):
        self.que = []
    def appendx(self,x):
        self.que.append(x)
    def rem(self):
        if len(self.que)>0:
            del self.que[-1]
    def pop(self):
        s = self.que[0]
        self.que = self.que[1:]
    def push(self,x):
        for i in range(len(self.que),0,-1):
            if self.que[i-1][0]<x[0]:
                self.rem()
            else:
                break
        self.que.append(x)
class Solution:
    def maxSlidingWindow(self, nums, k):
        if k == 0:
            return []
        if k == 1:
            return nums
        if len(nums)<=k:
            return [max(nums)]
        q = Que()
        m = []
        for i in range(k):
            q.push((nums[i],i))
            print(q.que)
        for i in range(len(nums)-k+1):
            if q.que[0][1] == i-1:
                q.pop()
            q.push((nums[i+k-1],i+k-1))
            m.append(q.que[0][0])
        return m


s = Solution()
nums = [13]
k = 0
print(s.maxSlidingWindow(nums,k))