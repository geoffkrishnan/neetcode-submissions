"""
input:
    2D int array - heights
        heights[i] - height above sea level at (r, c)
output:
    all cells where water can flow from that cell to left/bottom edge AND top/right edge


bruteforce:
    try all cells in left column from bottom to top
    and then see if we can get to right

fails because o(n * m)^2 time complexity, searching on each cell does repeated work

clever way is to start from first row and first column and find every cell that connects to those cells add it to set

and then do the same for last row and last column add it to set

then the union of those sets must be able to reach both





"""


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r: int, c: int, visited: set, prev_height: int) -> None:
            if (
                r < 0
                or r == rows
                or c < 0
                or c == cols
                or (r, c) in visited
                or heights[r][c] < prev_height
            ):
                return

            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])
        
        
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])
        
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])
        
        both = pacific & atlantic
        return list(both)
        
        
            
            
