class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i)) # make a min heap behave like ammax heap
            if i >= k - 1: # window size xhausted
                while heap[0][1] <= i - k: # outside windopw
                    heapq.heappop(heap)
                output.append(-heap[0][0])
            return output

            # always heap when max min needed in constant time
            

