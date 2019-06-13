import random
class Solution:

    def __init__(self, nums):
        self.ori = nums
        self.nums = nums
        super(Solution,self).__init__()
    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.ori
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        self.nums = random.sample(self.nums,len(self.nums))
        return self.nums


s = Solution([1,2,3,4])
print(s.shuffle())
print(s.reset())
