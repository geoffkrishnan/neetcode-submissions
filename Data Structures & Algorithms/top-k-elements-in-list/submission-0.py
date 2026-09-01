class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums) #num -> freq
        min_heap = []
        for n, f in freq.items():
            heapq.heappush(min_heap, (f, n))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [num for _, num in min_heap]
        

        