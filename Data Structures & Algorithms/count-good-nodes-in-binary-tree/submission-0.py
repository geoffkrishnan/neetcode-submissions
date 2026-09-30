# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_along_path: int):
            if node is None:
                return 0
            
            if node.val >= max_along_path:
                max_along_path = node.val
                return dfs(node.left, max_along_path) + dfs(node.right, max_along_path) + 1
                
            return dfs(node.left, max_along_path) + dfs(node.right, max_along_path)
            
        return dfs(root, root.val)

        