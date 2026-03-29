# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not(root):
            return None
        
        # swap стоит совершать через temp из-за особенностей питона
        temp = root.left
        root.left = root.right
        root.right = temp
        
        # ПРОСТО ЕБАНУТЫЙ ШОК КОНТЕНТ - МЫ МОЖЕМ НЕ СОЗДАВАТЬ НОВУЮ ФУНКЦИЮ А ВЫЗВАТЬ ТУ ЖЕ САМУЮ 
        # ПОТОМУ ЧТО ЭТО И ЕСТЬ ФУНКЦИЯ СВАПА АХУЕТЬ

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

