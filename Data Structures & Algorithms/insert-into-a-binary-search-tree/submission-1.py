# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp = TreeNode(val)
        def dfs(root, parent, direction):
            if root is None:
                match direction:
                    case "left":
                        parent.left = temp
                    case "right":
                        parent.right = temp
                    case "":
                        root = TreeNode(val)
                        return root
                return
            if val <= root.val:
                dfs(root.left, root, "left")
            else:
                dfs(root.right, root, "right")

        res = dfs(root, root, "")
        if res == None: return root 
        else: return res