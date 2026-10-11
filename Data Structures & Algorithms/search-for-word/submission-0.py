"""
input:
    2D string array - board
        board[i] = lower and uppercase english letters
                   dupe chars allowed
    string - word
        word[i] = lower and uppercase english letters

output:
    true if word in board else false

board has uppercase letters

word in board if
    path can be formed from letters in grid with horizontal/vertical neighbors

bruteforce:
    i = 0
    iter through grid to find the word[i]
    check neighbors to see if word[i + 1] exists
    if it does, recurse on word[i + 1]
    otherwise return

    must try every neighbor cuz could have multiple valid i + 1 neighbors but not every valid i + 1 neighbor will lead to word

    if we reach a dead end, return False
    if we reach the final letter, return True


"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, i):
            if i == len(word):
                print("found")
                print(r, c)
                return True
                
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or (r, c) in visited
                or board[r][c] != word[i]
            ):
                print("oob")
                return False


            found = False
            visited.add((r, c))
            for dr, dc in directions:
                if dfs(r + dr, c + dc, i + 1):
                    found = True
                    break

            
            visited.remove((r, c))
            return found

        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if dfs(r, c, 0):
                    return True
        return False
