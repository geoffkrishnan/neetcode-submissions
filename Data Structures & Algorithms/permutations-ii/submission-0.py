class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        unique_permutations = []
        path = []
        chosen_idx = set()
        nums.sort()

        def backtrack():
            if len(path) == len(nums):
                unique_permutations.append(path.copy())
                return
            
            for i in range(len(nums)):
                if i in chosen_idx:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and i - 1 not in chosen_idx:
                    continue

                path.append(nums[i])
                chosen_idx.add(i)
                backtrack()
                chosen_idx.remove(i)
                path.pop()
        
        backtrack()
        return unique_permutations
        
        