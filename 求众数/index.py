def index(nums):
    N = int((len(nums)+1)/2)
    #print(N)
    an_ls = []
    dic = {}
    for i in nums:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for j in dic:
        if dic[j]>=N:
            an_ls.append(j)
    return(an_ls[0])

l = [2,2,3]
s = [2,2,2,3,3,3]
print(index(l))
print(index(s))