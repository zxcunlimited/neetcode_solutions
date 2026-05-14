# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import sys
sys.setrecursionlimit(10 ** 6)

class Solution:
    res = ListNode()
    cur = res
    prev = cur
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists == []:
            self.prev.next = None
            return
        self.cur.next = ListNode()
        elems = {}
        i = 0
        for l in lists:
            elems[l.val] = i
            i += 1
        min_elem = min(elems)
        self.cur.val = min_elem
        self.prev = self.cur
        self.cur = self.cur.next
        lists[elems[min_elem]] = lists[elems[min_elem]].next
        self.mergeKLists([l for l in lists if l != None])
        return self.res