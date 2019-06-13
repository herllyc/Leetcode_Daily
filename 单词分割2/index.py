def wordBreak(s,wordDict):#超出时间限制,加上单词分割1的判断就可以
    if not s:
        return [[]]
    ans = []
    for i in range(len(s)+1):
        #ans = []
        for j in wordDict:
            if s[0:i]==j: 
                x = wordBreak(s[i:],wordDict)
                if x:
                    for j in x:
                        ans.append([s[0:i]]+j)
    return ans
    #return False
def index(s,wordDict):
    ls = wordBreak(s,wordDict)
    res = []
    for l in ls:
        res.append(' '.join(l))
    return res


print(index('catsanddog',["cat", "cats", "and", "sand", "dog"]))