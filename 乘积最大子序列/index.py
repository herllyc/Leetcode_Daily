class Solution:
    def maxProduct(self, nums):
        max_num = nums[0]
        min_num = nums[0]
        real_max = max_num
        for i in nums[1:]:
            if i<0:
                max_num,min_num = min_num,max_num
            max_num = max(max_num*i,i)
            min_num = min(min_num*i,i)
            print(max_num,min_num)
            real_max = max(real_max,max_num)
            print(real_max)
        return real_max




s = Solution()
nums = [2,3,-1,2,-5]
print(s.maxProduct(nums))
        