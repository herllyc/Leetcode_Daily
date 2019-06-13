class Solution:
    def increasingTriplet(self, nums):
        former,later,middle = nums[0],nums[0],nums[0]
        if len(nums)<3:
            return False
        for i in range(len(nums)-2):
            if nums[i]<=former and nums[i+1]>=nums[i]:
                former = nums[i]
                for j in range(i,len(nums)-1):
                    if nums[j]>former:
                        middle = nums[j]
                        for k in range(j+1,len(nums)):
                            if nums[k]>middle:
                                later = nums[k]
                                return (former,middle,later)
        return False


s = Solution()
print(s.increasingTriplet([5,1,5,5,2,5,4]))

                
