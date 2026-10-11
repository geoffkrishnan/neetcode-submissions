class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        path = []
        curr_sum = 0
        candidates.sort()

        def backtrack(curr_sum: int, curr_idx: int) -> None:
            if curr_sum == target:
                combinations.append(path.copy())
                return

            for i in range(curr_idx, len(candidates)):
                if candidates[i] + curr_sum > target:
                    break
                if i > curr_idx and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(curr_sum + candidates[i], i + 1)
                path.pop()

        backtrack(0, 0)
        return combinations
