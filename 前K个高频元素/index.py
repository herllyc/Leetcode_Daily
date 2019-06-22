import heapq


class Solution:
    def topKFrequent(self, nums, k):
        heap_max = []
        dic_fre = {}
        ans = []
        for i in nums:
            if i in dic_fre:
                dic_fre[i]+=1
            else:
                dic_fre[i] = 1
        for i in dic_fre:
            heapq.heappush(heap_max,(-dic_fre[i],i))
        for j in range(k):
            p = heapq.heappop(heap_max)
            ans.append(p[1])
        return ans

s= Solution()
nums = [1]
k = 1
print(s.topKFrequent(nums,k))