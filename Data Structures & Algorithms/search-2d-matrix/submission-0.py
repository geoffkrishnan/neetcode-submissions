class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            if self.binarySearch(matrix[i], target):
                return True
        
        return False
            

    def binarySearch(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                print(nums[mid])
                print("why")
                return True
            
            # 1 2 3 4 
            elif nums[mid] > target:
                r = mid - 1

            else:
                l = mid + 1

        return False


        