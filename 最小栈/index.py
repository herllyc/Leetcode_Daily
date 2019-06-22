class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stac = []

    def push(self, x):
        if self.stac:
            s = min(x,self.stac[-1][1])
            self.stac.append((x,s))
        else:
            self.stac.append((x,x))
        print(self.stac)
    def pop(self):
        self.stac.pop()

    def top(self):
        return self.stac[-1][0]

    def getMin(self):
        if self.stac:
            return self.stac[-1][1]
        else:
            return None
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
s = MinStack()
s.push(1)
s.push(2)
s.push(0)
print(s.top(),s.getMin())
s.pop()
print(s.top(),s.getMin())
