def merge(nums1,m,nums2,n):
    num1 = nums1[0:m]
    num2 = nums2[0:n]
    ls = []
    i = 0
    j = 0
    while True:
        if i == m:
            ls+=num2[j:]
            return(ls)
        if j == n:
            ls+=num1[i:]
            return(ls)
        if num1[i]>num2[j]:
            ls.append(num2[j])
            j+=1
        else:
            ls.append(num1[i])
            i+=1
        if len(ls)==(m+n):
            return(ls)


print(merge([1,2,3,0,0,0],3,[2,5,6],3))


