# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        isSame = False
        sub = subRoot
        
            
        def dfs(node):
            nonlocal isSame
            if isSame:
                return
            if node is None:
                return
            if node.val == subRoot.val:
                isSame = same(node, sub)
            dfs(node.left)
            dfs(node.right)
        
        def same(node, sub):
            if node is None and sub is None:
                return True
            
            if node is None or sub is None:
                return False
            
            if node.val != sub.val:
                return False
            
            return same(node.left, sub.left) and same(node.right, sub.right)
        
        dfs(root)


        return isSame

            
        
            

                
                

        