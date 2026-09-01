class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_count_to_anagrams = defaultdict(list)
        grouped_anagrams = []
        for string in strs:
            char_count = [0] * 26
            for char in string:
                char_count[ord(char) - ord('a')] += 1
            char_count = tuple(char_count)
            char_count_to_anagrams[char_count].append(string)
        for anagrams in char_count_to_anagrams.values():
            grouped_anagrams.append(anagrams)
        return grouped_anagrams