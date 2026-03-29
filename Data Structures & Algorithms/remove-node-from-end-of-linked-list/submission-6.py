# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # решение через два указателя, почти что как в оригинальном
        # if head.next == None:
        #     return None
        # slow, fast = head, head.next
        # count = 1
        # while fast.next != None:
        #     count += 1
        #     fast = fast.next
        # if (count - n) < 0:
        #     return head.next
        # for i in range(count - n):
        #     slow = slow.next
        # slow.next = slow.next.next
        # return head

        # решение через два указателя но поумнее - с созданием "болванчика" и нормальными двумя указателями
        dummy = ListNode(0, head)
        dummy.next = head
        l = dummy
        r = head
        for i in range(n):
            r = r.next
        while r:
            l = l.next
            r = r.next
        l.next = l.next.next
        return dummy.next