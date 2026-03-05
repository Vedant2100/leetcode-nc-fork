class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # whenever multiple inputs may wait for one condition
        # we use a stack
        
        stack = []
        res = [0] * len(temperatures) # tAKES CARE OF ELSE 
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                _, index = stack.pop()
                res[index] = i - index
            stack.append((temperatures[i], i))
        return res


