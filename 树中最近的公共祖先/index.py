# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.h = []
    def findway(self,root,t,v):
        if not root:
            return None
        v+=[root]
        if root.val==t.val:
            self.h = []+v
            #print(self.h)
            del v[-1]
            return None
        l = self.findway(root.left,t,v)
        r = self.findway(root.right,t,v)
        #print(self.h)
        if l:
            return l
        elif r:
            return r
        else:
            del v[-1]
            return None
    def lowestCommonAncestor(self, root, p, q):
        self.findway(root,p,[])
        wp = []+self.h
        wq= self.findway(root,q,[])
        wq = []+self.h
        for i in wp[-1::-1]:
            for j in wq[-1::-1]:
                print(i.val,j.val)
                if i.val==j.val:
                    return i