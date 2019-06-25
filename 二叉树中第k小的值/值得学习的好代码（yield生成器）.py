class Solution:
    def kthSmallest(self, root, k):
        from itertools import chain, islice
        def gen(x): yield from chain(gen(x.left), [x.val], gen(x.right)) if x else ()
        return next(islice(gen(root), k - 1, k))

链接：https://leetcode-cn.com/problems/two-sum/solution/3xing-python-sheng-cheng-qi-yield-by-knifezhu/
