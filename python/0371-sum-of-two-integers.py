class Solution:
    def twoSum(self, numbers:List[int], target: int):
        l, r = 0, len(numbers) - 1
        while l < r:
            cursum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l+1, r+1] # 1 indexed
        return []
# two pointers, hashmap, binary search 

