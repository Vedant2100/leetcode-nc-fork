class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # DP Kadance O(n)
        curSum = 0
        best_sum_i = [0] * len(nums)
        for i in range(len(nums)):
            curSum += nums[i]
            if curSum > nums[i]:
                best_sum_i[i] = curSum
            else:
                best_sum_i[i] = nums[i]
                curSum = nums[i]
        return max(best_sum_i)