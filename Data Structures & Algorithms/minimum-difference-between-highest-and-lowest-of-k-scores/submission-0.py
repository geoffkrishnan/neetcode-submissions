"""
nums[i]
k
"""

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_diff = float('inf')

        left = 0
        right = k - 1

        while right < len(nums):
            min_diff = min(nums[right] - nums[left], min_diff)
            left += 1
            right += 1


        return min_diff

        

        



        




        