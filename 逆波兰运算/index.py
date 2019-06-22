class Solution:
    def evalRPN(self, tokens):
        mid = []
        for i in tokens:
            if not mid:
                mid.append(int(i))
                continue
            if i =='+':
                x = mid[-1]
                y = mid[-2]
                s = y+x
                del mid[-1]
                del mid[-1]
                mid.append(s)
                continue
            if i =='-':
                x = mid[-1]
                y = mid[-2]
                s = y-x
                del mid[-1]
                del mid[-1]
                mid.append(s)
                continue
            if i =='*':
                x = mid[-1]
                y = mid[-2]
                s = y*x
                del mid[-1]
                del mid[-1]
                mid.append(s)
                continue
            if i =='/':
                x = mid[-1]
                y = mid[-2]
                s = int(y/x)
                del mid[-1]
                del mid[-1]
                mid.append(s)
                continue
            mid.append(int(i))
        return mid[0]

s = Solution()
t = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(s.evalRPN(t))