class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # O(nlogn)
        res = [] 

        def twoSumSorted(nums, target):
            duplets = []
            l, r = 0, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    duplets.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1 # optim 1 for repeats
            return duplets

        for i, a in enumerate(nums):
            if a > 0: # optim 2
                break
            if i > 0 and a == nums[i - 1]:
                continue # optim 3 for repeats

            duplets = twoSumSorted(nums[i + 1:], -a)
            for pair in duplets:
                res.append([a] + pair)

        return res