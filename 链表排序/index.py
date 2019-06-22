#NlogN-->归并、快速、堆排序
#O(1)-->归并、快速
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def to_left(self,todo):
        head.next = todo.next
        todo.next = head
        return todo
    def sortList(self, head):
        self.left = head
        while True:
            if head.next == None:
                return head
            if head.val>head.next.val:
                self.to_left(head,head.next)


n = ListNode(1)
n.next = ListNode(2)