class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0 
        while l < r:
            res = max((r - l)* min(height[l], height[r]), res)
            # retain longer bar 
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
