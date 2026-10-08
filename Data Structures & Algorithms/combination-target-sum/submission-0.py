"""
input:
    int array - nums
        distinct
        nums[i] - [2, 30]

    int - target, [2, 30]

output:
    list of all UNIQUE combinations of nums where the chosen numbers sum to target

same number may be chosen from nums an unlimited number of times

combinations are not unique if frequency of each of chosen nums is same, otherwise different


combinations may be in any order, order of nums in each combo may be in any order


"""
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []
        path = []
        nums.sort()

        def backtrack(start, remaining):
            if sum(path) >= target:
                if sum(path) == target:
                    combinations.append(path.copy())
                return
            
            for i in range(start, len(nums)):
                if sum(path) + nums[i] > target:
                    continue
                path.append(nums[i])
                backtrack(i, remaining - nums[i])
                path.pop()

            
        backtrack(0, len(nums))
        return combinations
        