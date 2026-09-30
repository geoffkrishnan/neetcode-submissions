# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        num_nodes_to_visit, kth_smallest = k, root.val

        def dfs(node: Optional[TreeNode]):
            nonlocal num_nodes_to_visit, kth_smallest

            if node is None:
                return
            
            dfs(node.left)

            if num_nodes_to_visit == 0:
                return
                
            num_nodes_to_visit -= 1
            if num_nodes_to_visit == 0:
                kth_smallest = node.val
                return
            
            dfs(node.right)

        dfs(root)
        return kth_smallest


            
            
        
        