# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        self.levels = []

        def bfs(root, level):
            if not(root):
                return
            if len(self.levels) <= level:
                self.levels.append([root.val])
            else:
                self.levels[level].append(root.val)
            bfs(root.left, level + 1)
            bfs(root.right, level + 1)

        bfs(root, 0)
        return self.levels