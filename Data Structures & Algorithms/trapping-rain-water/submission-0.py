"""
input:
    int array- height
        height[i] >= 0
        represents height of bar of width 1
output:
    total amount of water that can be fit between bars

so the amount of water depends on the the lower of two bars

so between an interval [a, b] where a and b are heights of bars

3 1 3

so the total area would be 1

so the difference between the two bars

"""
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_wall, right_wall = height[l], height[r]
        water = 0

        while l < r:
            if left_wall < right_wall:
                l += 1
                left_wall = max(left_wall, height[l])
                water += left_wall - height[l]
            else:
                r -= 1
                right_wall = max(right_wall, height[r])
                water += right_wall - height[r]
        return water
        
        