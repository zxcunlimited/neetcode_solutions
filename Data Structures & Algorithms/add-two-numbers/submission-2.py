# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # n1, n2 = 0, 0
        # i = 0
        # cur1, cur2 = l1, l2
        # while cur1 and cur2:
        #     n1 += cur1.val * (10 ** i)
        #     n2 += cur2.val * (10 ** i)
        #     i += 1
        #     cur1, cur2 = cur1.next, cur2.next
        # # несоблюдение dry, но мне лень ес честно
        # while cur1:
        #     n1 += cur1.val * (10 ** i)
        #     i += 1
        #     cur1 = cur1.next
        # while cur2:
        #     n2 += cur2.val * (10 ** i)
        #     i += 1
        #     cur2 = cur2.next

        # res = n1 + n2
        # new_head = ListNode()
        # new_head.val = res % 10
        # res //= 10
        # cur = new_head
        # while res:
        #     newnode = ListNode()
        #     newnode.val = res % 10
        #     res //= 10
        #     cur.next = newnode
        #     cur = cur.next
        # return new_head


        # то было типичное итеративное решение но сейчас папочка покажет мастер класс
        carry = ListNode()
        cur = carry
        s = 0
        while l1 or l2:

            s += l1.val if l1 else 0
            s += l2.val if l2 else 0

            new = ListNode(s % 10)
            s //= 10
            cur.next = new
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if s != 0:
            cur.next = ListNode(s % 10)

        return carry.next
