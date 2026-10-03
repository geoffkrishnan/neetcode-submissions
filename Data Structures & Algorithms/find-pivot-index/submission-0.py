class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        prefix sums suffix sums 

        """
        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]
        
        for i in range(len(nums)):
            sum_to_i = prefix[i]
            sum_from_end_to_i_plus_1 = prefix[len(nums)] - prefix[i + 1]

            if sum_to_i == sum_from_end_to_i_plus_1:
                return i

        return -1


        



        