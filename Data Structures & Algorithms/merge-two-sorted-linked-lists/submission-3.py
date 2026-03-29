# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        cur = new_head
        while list1 and list2:
            if list1.val >= list2.val:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next
            cur = cur.next
        # 1 версия дохода до конца если длины списков не одинаковые
        # while list1:
        #     cur.next = list1
        #     cur = cur.next
        #     list1 = list1.next
        # while list2:
        #     cur.next = list2
        #     cur = cur.next
        #     list2 = list2.next
        # cur.next = None
        # return new_head.next
        ''' 2 версия - можно упростить, так как у нас остался только один не пустой лист, а все
        следующие его узлы указывают на оставшиеся значения, то мы можем просто указать на 
        этот список и все
        '''
        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2
        # тут уже нет cur.next = None, так как мы закрепили за next указатель на список
        return new_head.next

