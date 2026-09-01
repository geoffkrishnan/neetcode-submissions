class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for index, value in enumerate(nums):
            if value in complements:
                return [complements[value], index]
            complements[target - value] = index 
        """
        for num in nums
            store target - num as key and current index as value
            {4: 0} 
            if num in dict:
                yes 4 is in dictionary.
                return current index and dict[num]
            
        """

            

            