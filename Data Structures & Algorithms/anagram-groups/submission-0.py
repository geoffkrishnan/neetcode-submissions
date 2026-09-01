from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        """
        char_count_to_anagrams = defaultdict(list)
        grouped_anagrams = []
        for string in strs:
            char_count = [0] * 26
            for char in string:
                char_count[ord(char) - ord('a')] += 1
            key = tuple(char_count)
            char_count_to_anagrams[key].append(string)
        for anagrams in char_count_to_anagrams.values():
            grouped_anagrams.append(anagrams)
        return grouped_anagrams