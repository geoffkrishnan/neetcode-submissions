class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in freq_map.items():
            buckets[freq].append(num)

        top_k_freq = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                top_k_freq.append(num)
                if len(top_k_freq) == k:
                    return top_k_freq


        

        