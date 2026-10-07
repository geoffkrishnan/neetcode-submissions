"""
a
aba
ababa
aa


"""
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(a, b):
            if len(a) > len(b):
                return False

            for i in range(len(a)):
                if a[i] != b[i]:
                    return False
            
            j = 0
            for i in range(len(b) - len(a), len(b)):
                if a[j] != b[i]:
                    return False
                j += 1

            return True

        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1
        return count
        

        