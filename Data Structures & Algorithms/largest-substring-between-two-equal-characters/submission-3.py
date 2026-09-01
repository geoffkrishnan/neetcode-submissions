"""
input:
    string - s
output:
    int - len of longest substring between two equal characters excluding those two characters else -1

we need the distance between the first and last occurrence of a character that appears at least 2 times


so for every character that appears at least 2 times:
    store the index of its first appearance
    iter through rest of the string and update the index of every subsequent appearance
    by the end of the iter, that should be last index

abca
0123
we want to output 2
last - first - 1


"""
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        freq_map = Counter(s)
        candidates = set()
        first_index = 0
        last_index = 0
        first_appearance = True
        max_len = -1

        for char, freq in freq_map.items():
            if freq >= 2:
                candidates.add(char)
        
        if not candidates:
            return max_len
        
        for char in candidates:
            first_appearance = True
            first_index = 0
            last_index = 0
            for i in range(len(s)):
                if first_appearance and s[i] == char:
                    first_appearance = False
                    first_index = i
                elif s[i] == char:
                    last_index = i
            max_len = max(max_len, last_index - first_index - 1)

        return max_len