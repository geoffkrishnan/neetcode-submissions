class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        num_islands = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or grid[r][c] == "0":
                return
            
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if (r, c) not in visited and grid[r][c] == "1":
                    num_islands += 1
                    dfs(r, c)
        return num_islands
        