class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # subarray is contiguous
        sumfuck = 0
        l = 0
        if len(nums) == 1 :
            return 0 if nums[0] < target else 1
        if sum(nums) < target:
            return 0
        minLen = len(nums)
        for j in range(len(nums)):
            sumfuck += nums[j]
            while sumfuck >= target:
                minLen = min(minLen, j-l+1)
                if minLen == 1:
                    break
                sumfuck -= nums[l]
                l += 1
        return minLen