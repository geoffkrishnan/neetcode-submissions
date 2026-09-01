class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_seq_len = 0
        nums_set = set(nums)
        for num in nums:
            if (num - 1) not in nums_set:
                curr_len = 1
                next_num = num + 1
                while next_num in nums_set:
                    curr_len += 1
                    next_num += 1
                longest_seq_len = max(curr_len, longest_seq_len)
        
        return longest_seq_len

        