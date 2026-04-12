# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.res = 0

        def dfs(root, visited: list, ):
            if root is None:
                return

            if visited == [] or max(visited) <= root.val:
                self.res += 1
            
            dfs(root.left, visited + [root.val])
            dfs(root.right, visited + [root.val])
        
        dfs(root, [])
        return self.res