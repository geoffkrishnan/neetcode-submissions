"""
dfs from every 1 returning area
keep the max
return max
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_area = 0

        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                grid[r][c] = 0
                area = 1
                for dr, dc in directions:
                    area += dfs(r + dr, c + dc)
                return area
            else:
                return 0
        
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if  val == 1:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area




        
        
        
        