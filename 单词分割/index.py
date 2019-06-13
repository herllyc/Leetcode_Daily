class Solution:
    def wordBreak(self, s, wordDict):
        def maxlen(wordDict):
            maxlen = 0
            for i in wordDict:
                maxlen = max(len(i),maxlen)
            return maxlen
        max_l = maxlen(wordDict)
        def index(s,wordDict,max_l):
            wordDict.sort(reverse=True)
            print(s)
            max_l = min(max_l,len(s))
            if not s:
                return 1
            i = 0
            l = 0
            while i<len(s)+1:
                i+=1
                for j in wordDict:
                    if(s[0:i]==j) and index(s[i:],wordDict,max_l):
                        l = 1
            return l
        return(bool(index(s,wordDict,max_l)))


if __name__ == '__main__':
    ind = Solution()
    iss = ind.wordBreak('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab',['a','aa','aaa'])
    print(iss)