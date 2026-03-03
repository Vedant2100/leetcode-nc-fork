class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # onlogn using sort
        # o(n) cycle detectionusing LL
        slow = nums[0]
        fast = nums[0]

        while True: # same loop as below but have to qeite differently, coz they are same at start
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: 
                break

        # one ptr at meeting place

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow

        