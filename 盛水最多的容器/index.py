def maxA(height):
    N = len(height)
    ls_f = [[0] * N for _ in range(N)]
    Max = 0
    if N<2:
        return('太短了')
    for i in range(N):
        for j in range(N):
            if i==j:
                continue
            else:
                ls_f[i][j]=abs(i-j)*min(height[i],height[j])
                Max = max(Max,ls_f[i][j])
    return(Max)




if __name__ == '__main__':
    ls = [1,8,6,2,5,4,8,3,7]
    maxA(ls)