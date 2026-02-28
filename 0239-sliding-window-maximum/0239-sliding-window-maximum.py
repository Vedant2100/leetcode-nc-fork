class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # heap for keeping track of maximum
        heap = []
        res = []

        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))

            while heap[0][1] <= i-k:
                heapq.heappop(heap) # “If the maximum element’s index is outside the window, remove it.” lazy deletion
            
            if i >= k-1: # window completed, record max
                res.append(-heap[0][0])
        return res

        