"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        clone = {}
        clone[node] = Node(node.val)
        q = deque([node])

        while q:
            curr_node = q.popleft()
            for n in curr_node.neighbors:
                if n not in clone:
                    clone[n] = Node(n.val)
                    q.append(n)
                clone[curr_node].neighbors.append(clone[n])

        return clone[node]  