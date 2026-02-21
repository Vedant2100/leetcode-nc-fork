class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break # coz sorted and positive doesnt sum to zero

            if i > 0 and a == nums[i-1]: # its not a circular array 
                continue # skip repeat elems because they'll produce same triplets with other two elems

            l, r = i+ 1, len(nums) - 1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l+=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1 # coz thats the only wy to possibly keep the sum constnat
                    while nums[l] == nums[l-1] and l < r:
                        l+=1 # skip repeats again

        return res


