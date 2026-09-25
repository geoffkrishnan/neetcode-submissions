"""
input:
    string s - uppercase english
    int k
output:
    length of longest substring with only 1 distinct char after replacing at most k chars

ops:
    choose up to k chars and replace with any other uppercase English char


bruteforce:
    maybe hmm.

pointer on each end of substring

decrement right pointer until substring[left] == substring[right]
    if it doesn't happen

increment left pointer then repeat until it does.

since there could be a case where it doesn't, only increment left pointer len(substring) - k times

then the minimum length must be at least k + 1

lets test so ABCD k = 2. k min is always 3

okay sure.

when those pointers are equal
by doing right - left + 1 we can know how many characters are between the first and last appearance of that character

well even if we do that it doesnt guarantee we know the optimal replacements


10 min in used 2 hints so hint is saying freq map

within a substring, the most optimal character to replace is the most frequent character. that's true.

okay. lets say we start with the entire string 

XYYX, k = 2

ok we can make a frequency map
x:2
y:2

both are optimal to replace within this substring

so since we can do 2 replacements then we get 4

when the current longest substring is equal to the length of the string then it has to be the max possible so can stop there


what about XCYYX, k = 1 

start with 
x - 2
y - 2
c - 1

Oh right when there are elements more frequent than other elements, than you place the less frequent with tho more frequent

so can replace C with X OR Y

if replace C with X it doesn't craete but it does with Y

the issue is that its substring so it must be like adjacent 

that's the part i don't really understand how to track.

don't we also need to know like after replacing is that substring actually like a contiguous sequence of repeats?


5 more min ill use up the rest of the hints

hint 3 - num replacements == len_current_substring - freq of most frequent
bruteforce would be consider all substrings use hashmap and return max len of substring that has at most k replacements


yeah so im on the right track but the thing is how do we consider all substrings efficiently. i still have no idea

hint 4
"sliding window. i mean i know its a sliding window problem but im still confused
dynamic window size and we will strink the window when num replacements exceeds k"

i don't understand how i would code that


[ABBCBCBCABA], k = 3

if we're shrinking then entire string must be the first substring we check

window = ABBCBCBCABA
okay. in that window we know 
A - 3
B - 5
C - 3

we have k - 3

oh. I guess like we don't need to know which between A or C to replace.

we just want to return the LENGTH so as long as we know the length is 

5 + 3 = 8 we can just return 8 and go next

lets say k was 2. then it would be 7?

what about XCYYX, k = 2

x - 2
y - 2
c - 1
so the longest possible would just be 2 + 1 = 3

wait so in what case does window ever shrink


AAAONOOOUTHENUTHENUTHEUNTHAAE

A - 5
O - 4
E - 4
N - 4
T - 4
H - 4

well. let's say k is 2

well. longest is not 7 in this case its 6

yeah time up gotta look at solution
i

so i'm completely off base in how to actually implement sliding window in this case

the way to check all substrings is 

left and right at start, incerement right and then start decrementing left.

seems obv when i got solution explained  but i just don't have this pattern internalized
ill try for a few min to code myself and then look at code after

"""
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






        