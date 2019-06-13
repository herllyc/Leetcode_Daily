class Solution:
    def productExceptSelf(self, nums):
        ans = [1 for i in range(len(nums))]
        left = [1 for i in range(len(nums))]
        right = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            if i >0:
                left[i] = left[i-1]*nums[i-1]
        for j in range(len(nums))[::-1]:
            if j<len(nums)-1:
                right[j] *= right[j+1]*nums[j+1]
        s = map(lambda x,y:x*y,left,right)
        return s
        

s = Solution()
s.productExceptSelf([1,2,3,4])