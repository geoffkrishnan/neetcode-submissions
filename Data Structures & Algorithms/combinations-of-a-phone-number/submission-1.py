"""
input:
    string - digits
        digits[i] = [2, 9]
output:
    list of all possible letter combinations digits can represent in any order

each digit can map to set of chars

order matters, must be unique combinations, using each digit->char once


"""


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        digit_to_char_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        combos = []
        path = []

        def backtrack(idx):
            if len(path) == len(digits):
                combos.append("".join(path.copy()))
                return
            
            for char in digit_to_char_map[digits[idx]]:
                path.append(char)
                backtrack(idx + 1)
                path.pop()
        
        backtrack(0)
        return combos
