def isMatch(s,p):
    s_len = len(s)
    p_len = len(p)
    dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
    #print(dp)
    dp[0][0] = True
    for i in range(p_len):#配i=0时的True
            if p[i] == "*" and dp[0][i - 1]:
                dp[0][i + 1] = True
    print(dp)
    for i in range(s_len):
        for j in range(p_len):
            if p[j] == s[i] or p[j] == ".":
                dp[i + 1][j + 1] = dp[i][j]
            elif p[j] == "*":
                if p[j - 1] != s[i]:
                    dp[i + 1][j + 1] = dp[i + 1][j - 1]#忽略*
                if p[j-1] == s[i] or p[j-1] == ".":
                    dp[i+1][j+1] = (dp[i][j+1] or dp[i+1][j] or dp[i+1][j-1])#/多个/一个/忽略
    #print(dp)
    return dp[-1][-1]

s = 'aaa'
p = 'a*a'
print(isMatch(s,p))