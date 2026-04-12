# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # в принципе рабочее решение, но из-за max вырождается до O(N^2) по времени
        # self.res = 0

        # def dfs(root, visited: list, ):
        #     if root is None:
        #         return

        #     if visited == [] or max(visited) <= root.val:
        #         self.res += 1
            
        #     dfs(root.left, visited + [root.val])
        #     dfs(root.right, visited + [root.val])
        
        # dfs(root, [])
        # return self.res

        self.res = 0

        def dfs(root, visited):
            if root is None:
                return

            if visited == -101 or visited <= root.val:
                self.res += 1
            
            dfs(root.left, max(visited, root.val))
            dfs(root.right, max(visited, root.val))
        
        dfs(root, -101)
        return self.res