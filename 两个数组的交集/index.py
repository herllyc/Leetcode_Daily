class Solution:
    def intersect(self, nums1, nums2):
        mod_list = nums1
        fin_list = []
        for i in nums2:
            try:
                mod_list.remove(i)
            except ValueError:
                continue
            fin_list.append(i)
        return fin_list




s = Solution()
print(s.intersect([1,2,2,3],[1,2,2,2]))