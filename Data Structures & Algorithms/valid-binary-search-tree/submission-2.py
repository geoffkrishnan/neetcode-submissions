# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        def in_order(node):
            nonlocal prev
            if node is None:
                return True

            if not in_order(node.left):
                return False

            if prev is not None and prev.val >= node.val:
                return False
                
            prev = node
            return in_order(node.right)
        return in_order(root)
        
        