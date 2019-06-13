def maxA(height):
    l = 0
    r = len(height)-1
    Max = 0
    while l<r:
        if height[l]<=height[r]:
            Max = max(Max,(r-l)*height[l])
            l+=1
            continue
        if height[r]<height[l]:
            Max = max(Max,(r-l)*height[r])
            r-=1
            continue
    return(Max)


if __name__ == '__main__':
    ls = [1,8,6,2,5,4,8,3,7]
    print(maxA(ls))