# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.nodes = []
        def bfs(root, height):
            if root is None:
                return
            if len(self.nodes) - 1 < height:
                self.nodes.append([root.val])
            else:
                self.nodes[height].append(root.val)
            bfs(root.left, height + 1)
            bfs(root.right, height + 1)
        
        bfs(root, 0)
        return [i[-1] for i in self.nodes]