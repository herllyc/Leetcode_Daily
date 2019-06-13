def searchM(matrix,target):
    i = 0
    j = -1
    try:
        while True:
            s = matrix[i][j]
            if target==s:
                return True
            elif target<s:
                j-=1
            elif target>s:
                i+=1
    except IndexError:
        return False


ls = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
print(searchM(ls,31))