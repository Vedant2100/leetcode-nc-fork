class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        flag = False
        for i in range(0,len(nums)):
            n = nums[i]
            while n != 2**31 and 0<=n<len(nums):
                temp = nums[n]
                nums[n] = 2**31
                n = temp
                if n == len(nums):
                    flag = True
        
        i = 1
        print(nums)
        if len(nums) == 1:
            return nums[0]+1 if nums[0]==1 else 1
        while i<len(nums):
            if nums[i] != 2**31 or nums[i]<0:
                print(nums[i] < 0)
                break
            i+=1
        if nums[0] == i:
            return i+1

        if i == len(nums) and flag:
            return i+1

        return i

