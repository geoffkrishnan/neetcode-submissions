# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left_min, right_max):
            if node is None:
                return True
            
            if node.val >= left_min or node.val <= right_max:
                return False

            return dfs(node.left, node.val, right_max) and dfs(node.right, left_min, node.val)
        
        return dfs(root, float('inf'), float('-inf'))
        