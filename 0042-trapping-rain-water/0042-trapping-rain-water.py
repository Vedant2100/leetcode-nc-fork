class Solution:
    def trap(self, nums: List[int]) -> int:
        # water stored at i  =  min(nums[l], nums[r]) - nums[i] where l and r are the first ones bigger than nums[i] -NOTHING LIKE THAT
        # its simpler , just biggest ones to left and right

        # o(n2) for each i , find l and r  
        # water = [0]*len(nums)
        # for i in range(len(nums)):
        #     l, r = 0, len(nums) - 1
        #     maxl, maxr = 0, 0
        #     while l < i:
        #         maxl = max(maxl, nums[l])
        #         l += 1
        #     while r > i:
        #         maxr = max(maxr, nums[r])
        #         r -= 1
        #     water[i] = max(0, min(maxl, maxr) - nums[i]) # cant be. neg
        # return sum(water)

        # o(n) time and space
        prefix = [0] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = max(prefix[i - 1], nums[i - 1])
        suffix = [0] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], nums[i + 1])
        total = 0
        for i in range(len(nums)):
            water = min(prefix[i], suffix[i]) - nums[i]
            if water > 0:
                total += water
        return total

        

