class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        track = defaultdict(int)

        for i in nums:
            track[i] += 1
            
        # min heap - the smallest element is always at index 0, we want the 'top' or largest elements

        heap = []
        for i in track:
            heapq.heappush(heap, (track[i], i))
            if len(heap) > k:
                heapq.heappop(heap)
        # heap is now a k sized list of tuples (frequency, value)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res 

                