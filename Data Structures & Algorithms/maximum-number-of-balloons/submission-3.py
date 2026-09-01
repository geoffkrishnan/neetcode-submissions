class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word_freq = Counter("balloon")
        freq_map = Counter(text)
        num_balloons = float('inf')

        for char in word_freq.keys():
            num_balloons = min(num_balloons, freq_map[char] // word_freq[char])
        
        return num_balloons
