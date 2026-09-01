class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            if not self.isValid(board[r]):
                return False
        
        for c in range(cols):
            col = [board[r][c] for r in range(rows)]
            if not self.isValid(col):
                return False
        
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                box = []
                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        box.append(board[r][c])
                if not self.isValid(box):
                    return False

        return True

    def isValid(self, v):
        digits = self.filterDigits(v)
        return len(digits) == len(set(digits))
    
    def filterDigits(self, n):
        return [x for x in n if x != "."]
        