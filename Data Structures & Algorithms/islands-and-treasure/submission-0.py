"""
init idea:
    multisource bfs from treasure  chests


"""
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if v == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        directions = [(1, 0), (-1, 0), (0, 1), (0,-1)]
        distance = 0

        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                grid[x][y] = distance
                for dx, dy in directions: 
                    if 0 <= x + dx < rows and 0 <= y + dy < cols and ((x + dx, y + dy) not in visited) and grid[x + dx][y + dy] != -1:
                        q.append((x + dx, y + dy))
                        visited.add((x + dx, y + dy))

            distance += 1
    

        