"""
input:
    int - n
        number of nodes
    int array - edges
        edges[i] = [a, b]

output:
    number of connected components
"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node):
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        
        connected_components_count = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                connected_components_count += 1
        return connected_components_count
        
            

        