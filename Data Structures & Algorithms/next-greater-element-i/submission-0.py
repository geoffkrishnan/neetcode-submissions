"""
nums1 = 4, 1, 2
nums2 = 1, 3, 4, 2


okay. so for every element in nums1
    find the element in nums2 that is to the right and is > that element
    if none exists -1

"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greaters = []

        for num in nums1:
            j = nums2.index(num)
            for x in nums2[j:]:
                if x > num:
                    next_greaters.append(x)
                    break
                # how do i know if i didnt find a greater and add -1
            else:
                next_greaters.append(-1)
        

        return next_greaters

       