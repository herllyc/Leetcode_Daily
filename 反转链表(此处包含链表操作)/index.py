class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def p_l(node):#打印链表
    while node:
        print (node.val,end = '')
        print('->',end = '')
        node = node.next
def to_link(ls):#ls转链表
    node = ListNode(ls[0])
    f1 = node
    for i in ls[1:]:
        node2 = ListNode(i)
        node.next = node2
        node = node2
    return f1
def to_list(node):
    l = []
    while node:
        l.append(node.val)
        node = node.next
    return l
class Solution:
    def reverseList(self, head):
        if head.next == None:
            return head
        left = head
        mid = head
        todo = head.next
        while todo:
            mid.next = todo.next
            todo.next = left
            left = todo
            todo = mid.next
        return left



s = [1,2,3,4,5]
node = to_link(s)
#print(node)
#p_l(node)
so = Solution()
pp = so.reverseList(node)
l = to_list(pp)
print(l)