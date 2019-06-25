# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest1(self, root):
        if not root:
            return []
        s = self.kthSmallest1(root.left)+[root.val]+self.kthSmallest1(root.right)
        return s
    def kthSmallest(self,root,k):
        s = self.kthSmallest1(root)
        #s.sort()
        return s[k-1]