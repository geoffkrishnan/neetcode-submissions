"""
input:
    int array - heights

output:
    int - maximum amount of water a container can store

so. given that heights array represents the height of heights[i]th bar

can choose two bars to form a container.

the maximium amount of water stored in a container is determined by:
    - the smallest height between (bar1, bar2)
    - if chosen bars are at indices 1 and 7 then width of container is 
        7 - 1 = 6

area = width * height

want the max possible area.

can start at opposite ends of the array

whichever height is smaller maybe discard that one and increment/decrement that pointer
repeat until no more.
each time update max area

return max area does that work actually idk



"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right:
            smallest = min(heights[left], heights[right])
            area = smallest * (right - left)
            max_area = max(area, max_area)

            if smallest == heights[left]:
                left += 1
            else:
                right -= 1

        return max_area
            
        