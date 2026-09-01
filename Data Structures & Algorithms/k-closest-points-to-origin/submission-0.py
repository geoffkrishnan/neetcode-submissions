"""
input:
    points - list of lists
        points[i] = [x, y]
    is each point in the list unique?
    k - int
output:
    k number of points that are closest to [0, 0]

distance between two points is sqrt((x1 - y1)^2 - (x2 - y2)^2))

so we can just make a function to calculate the distance to origin for each point in the points list

we push these distances into a max heap. the closer the distance smaller number.

so if we do max heap, and then we pop n - k times, the remaining elements will be k smallest

which will be the k closest distances to the origin

we want to return the points those distances belong to.

so we can create a hashmap of distances to points.

well we can just do indices of points array where those points live


"""
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        def distanceToOrigin(point: List[int]) -> int:
            x, y = point
            return math.sqrt(x**2 + y**2)
        
        for point in points:
            heap.append((distanceToOrigin(point), point))

        heapq.heapify_max(heap)

        while len(heap) > k:
            heapq.heappop_max(heap)

        points_closest_to_origin = []
        for i in range(k):
            _, point = heapq.heappop_max(heap)
            points_closest_to_origin.append(point)

        return points_closest_to_origin