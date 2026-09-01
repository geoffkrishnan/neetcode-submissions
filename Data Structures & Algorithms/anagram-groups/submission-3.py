class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = defaultdict(list)
        for string in strs:
            char_count = [0] * 26
            for char in string:
                char_count[ord(char) - ord('a')] += 1
            char_count = tuple(char_count)
            grouped_anagrams[char_count].append(string)
        return list(grouped_anagrams.values())