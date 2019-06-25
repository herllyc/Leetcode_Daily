class Solution:
    def fourSumCount(self, A,B,C,D):
        hash_A = {}
        for i in range(len(A)):
            for j in range(len(B)):
                s = A[i]+B[j]
                if s in hash_A:
                    hash_A[s].append((i,j))
                else:
                    hash_A[s] = [(i,j)]
        hash_B = {}
        for i in range(len(C)):
            for j in range(len(D)):
                s = C[i]+D[j]
                if s in hash_B:
                    hash_B[s].append((i,j))
                else:
                    hash_B[s] = [(i,j)]
        SUM = 0
        for k in hash_A:
            if -k in hash_B:
                SUM+=(len(hash_A[k])*len(hash_B[-k]))
        return SUM


s = Solution()
x = s.fourSumCount([1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,8])
print(x)