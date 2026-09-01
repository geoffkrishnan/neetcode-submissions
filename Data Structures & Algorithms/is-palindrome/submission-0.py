class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = s.lower()
        clean = ''.join(c for c in clean if c.isalnum())

        return clean[::-1] == clean
        