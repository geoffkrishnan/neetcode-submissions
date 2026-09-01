"""
input:
    string - s
output:
    int - maximum difference between odd and even frequency chars in s
constraints:
    must contain at least 1 odd and 1 even freq char

freq_map = Counter(s)

for every distinct character in the string:
    if its frequency is odd
        group it into an array
    else must be even
        group it

given a set of even numbers and a set of odd numbers,

how can we choose the two numbers that maximizes the difference between them.

hmm.

biggest number in evens - smallest number in odds OR smallest number in evens and biggest number in odds?
whichever is the max of those, would be the max difference between different parity freq chars in string

"""
class Solution:
    def maxDifference(self, s: str) -> int:
        freq_map = Counter(s)
        odd_max = float('-inf')
        even_min = float('inf')
        for freq in freq_map.values():
            if freq % 2 == 0:
                even_min = min(even_min, freq)
            else:
                odd_max = max(odd_max, freq)
        
        return odd_max - even_min

        


        