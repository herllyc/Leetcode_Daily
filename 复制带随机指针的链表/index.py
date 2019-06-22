null = None
class Solution:
    def copyRandomList(self, head):
        d = node(head.val,0,0)
        if type(head[i])==Node:
            d.next = self.copyRandomList(head[i])
        else:
            d.next = None
        d.random = self.copyRandomList(head.random)
        return d
