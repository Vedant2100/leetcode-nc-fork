class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax: 
                l += 1 # move the shorter bar
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            elif leftMax >= rightMax:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res


#         o for every position, we need:

# highest bar on the left

# highest bar on the right