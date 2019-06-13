class Solution:
    def containsDuplicate(self, nums):
        dic_l = {}
        for i in nums:
            if i in dic_l:
                return True
            else:
                dic_l[i] = 1
        return False
        