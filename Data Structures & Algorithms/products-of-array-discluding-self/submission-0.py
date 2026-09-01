class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = [0] * len(nums)
        suffix_products = [0] * len(nums)

        prefix_products[0] = 1
        for i in range(1, len(nums)):
            prefix_products[i] = prefix_products[i - 1] * nums[i - 1] 

        suffix_products[len(nums) - 1] = 1
        for i in range(len(nums) - 2, -1, -1):
            suffix_products[i] = suffix_products[i + 1] * nums[i + 1] 
        
        product_except_self = []
        for pp, sp in zip(prefix_products, suffix_products):
            product_except_self.append(pp * sp)



        return product_except_self

            