class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len, left = 0, 0
        last_seen = {}

        for right in range(len(s)):
            if s[right] in last_seen:
                left = max(last_seen[s[right]] + 1, left)
            last_seen[s[right]] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len
        