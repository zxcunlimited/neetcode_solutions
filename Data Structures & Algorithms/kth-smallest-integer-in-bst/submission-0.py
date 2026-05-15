# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from heapq import *

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.heap = []
        def dfs(root):
            if root is None:
                return
            heappush(self.heap, root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        while k > 1:
            heappop(self.heap)
            k -= 1
        return heappop(self.heap)