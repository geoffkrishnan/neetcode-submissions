"""
input:
    s1 - string
    s2 - string
    both lowercase English letters 
output:
    true if s2 contains permutation of s1 or false

s1 - abc s2 - def
false

s1 - abc s2 - bac
true

s1 - abc s2 - baac
false

Okay so my intial idea is

look through s2 with a fixed sliding window of len(s1)

if the freq map of that sliding window matches freq map of s1
    then true

after you finish looking through with window and didn't return true
must be false

what would that look like

s1_f s a-1, b-1, c-1

s2 - baac

so start with left pointer at 0 and right pointer at len(s1) - 1

baac
L R

A-2 B-1
so no
next
baac
 L R
A-2 c-1
no

done. return false

"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_len = len(s1)
        if window_len > len(s2):
            return False
        s1_f_map = Counter(s1)
        window = Counter(s2[:window_len])

        if window == s1_f_map:
            return True
        for right in range(window_len, len(s2)):
            window[s2[right]] += 1
            window[s2[right - window_len]] -= 1
            if window == s1_f_map:
                return True
            
        return False