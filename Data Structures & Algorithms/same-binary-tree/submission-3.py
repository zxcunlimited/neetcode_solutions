# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # tr1, tr2 = list(), list()

        # def dfs(root, l):
        #     if root is None:
        #         l.append("None")
        #         return 
        #     l.append(root.val)
        #     dfs(root.left, l)
        #     dfs(root.right, l)

        # dfs(p, tr1)
        # dfs(q, tr2)
        # print(tr1, tr2)
        # return tr1 == tr2

        def dfs(r1, r2):
            if not r1 and not r2:
                return True
            if not r1 or not r2:
                return False
            if r1.val != r2.val:
                return False
            return all([dfs(r1.left, r2.left), dfs(r1.right, r2.right)])
        
        return dfs(p, q)
            