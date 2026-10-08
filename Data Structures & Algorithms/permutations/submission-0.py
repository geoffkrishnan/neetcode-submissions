"""
input:
    int array - nums
    distinct ints
output:
    list of every possible permutations of nums in any order



"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        path = []
        seen = set()

        def backtrack():
            if len(path) == len(nums):
                permutations.append(path.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in seen:
                    continue
                path.append(nums[i])
                seen.add(nums[i])
                backtrack()
                path.pop()
                seen.remove(nums[i])
        
        backtrack()

        return permutations
            
        