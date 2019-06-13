class Solution:
    def isAnagram(self, s, t):
        dic1 = {}
        dic2 = {}
        for i in s:
            if i in dic1:
                dic1[i]+=1
            else:
                dic1[i] = 1
        for j in t :
            if j in dic2:
                dic2[j]+=1
            else:
                dic2[j] = 1
        return dic1==dic2
        # s = list(s)
        # t = list(t)
        # f1 = s.sort()
        # f2 = t.sort()
        # print(f1)
        # print(f2)
        # return f1 == f2









s = Solution()
print(s.isAnagram('b','a'))
