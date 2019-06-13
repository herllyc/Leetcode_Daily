class Solution:
    def firstUniqChar(self, s):
        def inner(s):
            dics = {}
            for i in range(len(s)):
                if s[i] not in dics:
                    dics[s[i]] = 1
                    if i == len(s)-1:
                        return i
                    j = i
                    while j<len(s)-1:
                        j+=1
                        if s[i] == s[j]:
                            break
                        if j == len(s)-1:
                            return i
        i = inner(s)
        if i is None:
            return -1
        else:
            return i



s = Solution()
print(s.firstUniqChar('z'))