# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(a, b):
            if a is None and b is None:
                return
            
            if a and b: 
                a.val += b.val
                a.left = dfs(a.left, b.left)
                a.right = dfs(a.right, b.right)
                return a
            
            if a is None and b:
                return b

            if a and b is None:
                return a
        
        return dfs(root1, root2)
""" 
a - None
b - 2

dfs(None, 2)
    return 2
""" 



        