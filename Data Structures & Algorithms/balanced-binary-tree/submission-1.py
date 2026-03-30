# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.balance = True
        def dfs(root):
            if not(root):
                return 0
            l = dfs(root.left) + 1
            r = dfs(root.right) + 1
            if max(r, l) - min(r, l) > 1:
                self.balance = False
            return max(l, r)

        res = dfs(root)
        return self.balance