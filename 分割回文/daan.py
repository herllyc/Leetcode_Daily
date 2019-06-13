def partition(s):
        if not s: return [[]]
        res = []
        for i in range(len(s)):
            temp = s[:i+1]
            if temp == temp[::-1]:
                for j in partition(s[i+1:]):
                    res.append([temp]+j)
        return res



print(partition('aab'))