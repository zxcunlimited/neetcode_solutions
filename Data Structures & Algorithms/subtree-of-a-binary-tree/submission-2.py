# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # в теории рабочее решение, локально работает но тут проваливает тест [1, 1] :/
        # def dfs(root, sub):
        #     if not(root) and not(sub):
        #         return True
        #     if not(root) or not(sub):
        #         return False
        #     if root.val != sub.val:
        #         return False
        #     return dfs(root.left, sub.left) and dfs(root.right, sub.right)

        # def start_dfs(root, sub):
        #     if not(root):
        #         return
        #     if root.val == sub.val:
        #         return dfs(root, sub)
        #     return start_dfs(root.left, sub) or start_dfs(root.right, sub)

        # if start_dfs(root, subRoot) in [None, False]:
        #     return False
        # return True

        if not subRoot: return True
        if not root: return False

        if self.sameTree(root, subRoot): return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def sameTree(self, root, sub):
        if not(root) and not(sub):
            return True
        if root and sub and root.val == sub.val:
            return (self.sameTree(root.left, sub.left) and self.sameTree(root.right, sub.right))
        return False