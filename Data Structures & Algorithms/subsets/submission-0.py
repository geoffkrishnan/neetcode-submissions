"""
input:
    int array - subsets
        unique ints
output:
    array of int array - all possible subsets of nums

init powerset list with empty subset
for num in nums
    copies = []
    for subset in powerset
        copies.append(subsset.copy())
    for copy in copies
        copy.append(num)
    powerset += copies
return powerset

"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerset = [[]]
        for num in nums:
            copies = []
            for subset in powerset:
                copies.append(subset.copy())
            for copy in copies:
                copy.append(num)
            powerset.extend(copies)
        return powerset

            
        
        