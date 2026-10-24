"""
input:
    int n - number of nodes [0, n - 1]
    int array - edges
        edges[i] = [n1, n2]

output:
    return True if edges make valid tree else False

what is valid tree?
- connected graph of nodes with no cycles
- must be one connected component
- n - 1 edges

if num edges != n - 1
    false

if cycle exists
    false

if fully connected  and num edges == n - 1
    true
else
    false




"""
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj_list = [[] for _ in range(n)]
        for i, j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)

        visited = set()
        def dfs(node: int, parent: int) -> bool:
            if node in visited:
                return False
            
            visited.add(node)
            for n in adj_list[node]:
                if n == parent:
                    continue
                if not dfs(n, node):
                    return False

            return True
        
        return dfs(0, -1) and len(visited) == n
        
    

        