"""
idea:
    dfs from every O on the edge of the board
        add each O connected to the edge O to set

    then iter through board marking everything X if its an O not in the connected set


"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        connected = set()

        def dfs(r, c):
            if (
                (r, c) in connected
                or r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or board[r][c] == "X"
            ):
                return
            
            connected.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
                
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)
        
        for r, row in enumerate(board):
            for c, _ in enumerate(row):
                if (r, c) not in connected:
                    board[r][c] = "X"