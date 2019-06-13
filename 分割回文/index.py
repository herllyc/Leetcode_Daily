def index(s):
    if not s:return [[]]
    ans =[]
    load = []
    for i in range(len(s)):
        if s[i]==s[0]:
            load.append(i)
    for j in load:
        h1 = s[0:j+1]
        h2 = s[j::-1]
        if h1==h2:
            for k in index(s[j+1:]):
                ans.append([h1]+k)
    return ans

print(index('aabaa'))