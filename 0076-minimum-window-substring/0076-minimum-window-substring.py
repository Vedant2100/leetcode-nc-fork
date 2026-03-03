class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # s has to have greq length than t
        if len(t) > len(s):
            return ""
        countT = Counter(t)
        minLen = float("inf") # cannot be len(s) for some reason.beacuse of strict ineq inside
        minSubst = "" # cannot be s for some reason
        # we start froma. window of size t
        countS = Counter() # empty 
        l = 0
        for j in range(len(s)): # we dont start from len(t) lol
            countS[s[j]] += 1 
            if countT <= countS:
                while countT <= countS:
                    if j-l+1 < minLen:
                        minLen = j-l+1               
                        minSubst = s[l:j+1]
                    countS[s[l]] -= 1
                    l += 1
        return minSubst


