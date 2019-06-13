class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return
        k = k%len(nums)
        F = nums[-k::1]
        L = nums[0:-k:1]
        nums[0:k] = F
        nums[k:] = L
        print(nums)
s = Solution()
s.rotate([1,2],0)