class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, maxf,len_longest, freq_count = 0, 0, min(len(s), k + 1), {}
        for r in range(len(s)):
            freq_count[s[r]] = 1 + freq_count.get(s[r], 0)
            maxf = max(maxf, freq_count[s[r]])
            while (r - l + 1) - maxf > k:
                freq_count[s[l]] -= 1
                l += 1
            len_longest = max(len_longest, r - l + 1)
        return len_longest






        