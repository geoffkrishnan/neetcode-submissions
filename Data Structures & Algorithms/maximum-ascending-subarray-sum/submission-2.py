"""
we want the maximum sum out of every possibly strictly increasing subarray

so need to identify every strictly increasing subarray
and count the sum of that. 
then need to track the max of all the sums

for i, num in nums starting from index 1
   if nums[i] is greater then nums[i - 1]:
      that means nums[i] contributes to strictly increasing sequence
      so we can add this nums[i] to curr_sum 
    update max_sum to max(max_sum, curr_sum)

"""

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr_sum += nums[i]
                max_sum = max(max_sum, curr_sum)
            else:
                curr_sum = nums[i]
                max_sum = max(max_sum, curr_sum)


        

        return max_sum

        