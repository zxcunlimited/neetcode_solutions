# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # рабочая хуйня, сложность O(N + (N - index)) (в худшем случае вырождается в 2N), по памяти такая же
        # self.nodes = list()
        # self.cycle = list()
        # def find_cycle(head):
        #     if head is None:
        #         return False
        #     if head.val in self.nodes:
        #         if self.cycle == []:
        #             self.cycle.append(head.val)
        #         else:
        #             if self.cycle[0] == head.val:
        #                 return True
        #             else:
        #                 self.cycle.append(head.val)
        #     else:
        #         self.nodes.append(head.val)
        #     return find_cycle(head.next)
        
        # res = find_cycle(head)
        # return res

        # отличное решение за O(N) и столько же по памяти
        cur = head
        completed = set()
        while cur:
            if cur in completed:
                return True
            completed.add(cur)
            cur = cur.next
        return False