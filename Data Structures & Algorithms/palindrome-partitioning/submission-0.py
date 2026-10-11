
"""
input:
    string s
output:
    lists of all possible palindromic substrings of s


how do we prune 


can always have a list of every character on its own because each character by itself is a palindrome

when we have a substring if we add a character if the resulting substring can't become a palindrome?

substring = consecutive sequence

so given aab

can either take a or skip a
skip a creates empty string which in this case doesn;t count as palindrome
take a. a is a palindrome


with a in path
can only take a. since it has to be consecutive
so aa. aa is palindrome

remaining. can't add it to current path because aab is not palindrome

return and then only remaining choice is b. add it.



"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromic_substrings = []
        path = []

        def backtrack(start):
            if start == len(s):
                palindromic_substrings.append(path.copy())
                return
            for i in range(start, len(s)):
                substring_to_add = s[start:i + 1]
                if substring_to_add != substring_to_add[::-1]:
                    continue
                
                path.append(substring_to_add)
                backtrack(i + 1)
                path.pop()
        backtrack(0)
        return palindromic_substrings
    
        