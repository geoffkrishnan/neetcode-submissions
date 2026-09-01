class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alphabet = [0] * 26

        for char in magazine:
            alphabet[ord('a') - ord(char)] += 1
        
        for char in ransomNote:
            alphabet[ord('a') - ord(char)] -= 1
            if alphabet[ord('a') - ord(char)] < 0:
                return False
        
        return True
        
        