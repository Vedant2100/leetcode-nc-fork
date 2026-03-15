class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        l = 0
        minSize = float('inf')
        for j in range(len(nums)):
            sum += nums[j]
            if sum >= target:
                while sum >= target:
                    if j-l+1 < minSize:
                        minSize = j - l + 1
                    sum -= nums[l]
                    l += 1
                    
        return 0 if minSize == float('inf') else minSize
