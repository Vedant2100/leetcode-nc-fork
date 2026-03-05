class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # instead of recalculating smallest to the left for every index,
        # the idea is store indices on stack, if someone comes to the right thats shorter, pop thwm off and record....
        left_stack = []
        right_stack = []
        n = len(heights)
        left_shorter = [-1] * n # defaults
        right_shorter = [n] * n
        for i in range(len(heights)):
            while right_stack and right_stack[-1][0] > heights[i]:
                _, ind = right_stack[-1]  # only index 
                right_shorter[ind] = i
                right_stack.pop()
            right_stack.append((heights[i], i)) # value not needed actually
        for j in range(len(heights)-1, -1, -1): # skip 0 if we stop at 0
            while left_stack and left_stack[-1][0] > heights[j]:
                _, ind = left_stack[-1] 
                left_shorter[ind] = j
                left_stack.pop()
            left_stack.append((heights[j], j))
        maxArea = float('-inf')
        for i in range(n):
            maxArea = max(maxArea, ((right_shorter[i] - 1) - (left_shorter[i] + 1)  + 1)* heights[i]) 
        return maxArea





        # for each index i , we can expand lef tor fight and try not to hit a smaller bar
        # so as to find the largest expabnded rectangle at that index
        # naive o(n2) TLE

        # broken into stack o(n)

        # maxArea = 0
        # for i in range(len(heights)):
        #     l, r = i, i
        #     while l >= 0 and r < len(heights):
        #         if heights[l] >= heights[i]:
        #             l -= 1
        #         if heights[r] >= heights[i]:
        #             r += 1
        #         maxArea = max(maxArea, (r-l+1)*heights[i]) 
        # return maxArea