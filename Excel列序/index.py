hash = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S':
19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}#提交偷了个鸡
h = {}#正常算hash表
x = 'A'
while ord(x)<=ord('Z'):
    h[x] = ord(x)-64
    x = chr(ord(x)+1)
class Solution:
    def titleToNumber(self, s):
        pos = 1
        res = 0
        for i in s[-1::-1]:
            res+=(hash[i]*pos)
            pos*=26
        return res
        


s = Solution()
print(s.titleToNumber('A'))