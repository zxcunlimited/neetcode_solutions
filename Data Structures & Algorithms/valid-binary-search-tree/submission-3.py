# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def spec_dfs(root, left, right):
            if not(root):
                return True
            if left < root.val < right:
                return spec_dfs(root.left, left, root.val) and spec_dfs(root.right, root.val, right)
            else:
                return False
    
        return (spec_dfs(root, float("-inf"), float("+inf")))