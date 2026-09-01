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
        evens = []
        odds = []
        for freq in freq_map.values():
            if freq % 2 == 0:
                evens.append(freq)
            else:
                odds.append(freq)
        
        # oh it HAS to be odd - even
        return max(min(odds) - max(evens), max(odds) - min(evens))


        