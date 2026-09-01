import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums] # o(n)
        heapq.heapify(max_heap) # o(n)
        for _ in range(k):
            kth_largest = heapq.heappop(max_heap)
        return -kth_largest
