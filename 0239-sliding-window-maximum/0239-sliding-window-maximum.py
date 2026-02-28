class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #O(N2) BRUTE
        # since keeping track ofmaximum , heaps needed 
        # O(NLOGN) with heap and thats the best. You could reconstruct heap everytme.
        # Below greedy which only cares about removing from heap if its aminimum
        # Its just heap istead of set and dict resp
        heap = []
        res = []
        for j in range(len(nums)):
            heapq.heappush(heap, (-nums[j], j)) # single pass heap populating
            if j >= k -1: #j outside 0 to k-1
                while heap and heap[0][1] <= j-k: # remove minimums if outside window
                    heapq.heappop(heap)
                res.append(-heap[0][0])
        return res
        