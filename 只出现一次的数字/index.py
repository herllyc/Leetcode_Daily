def index(nums):
    l = {}
    for i in nums:
        if i in l:
            del l[i]
        else:
            l[i]=1
    return (list(l.keys()))

print(index([2,2,3,2,2,3,5,5,1]))