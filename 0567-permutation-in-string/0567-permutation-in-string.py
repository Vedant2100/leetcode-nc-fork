class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # ininitlaly jut checked counts but thats not enough
        # so character alignment
        if len(s2) < len(s1):
            return False
        counts1 = Counter(s1)
        l = 0
        window= Counter()

        for r in range(len(s2)):
            window[s2[r]] += 1
            
            # Maintain a window of exactly length len(s1)
            if r - l + 1 > len(s1):
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    del window[s2[l]] 
                l += 1
            
            if window == counts1:
                return True
                
        return False
        # for j in range(len(s2)):
        #     if s2[j] not in s1:
        #         window = Counter()
        #         continue
        #     window[s2[j]] = window.get(s2[j],0) + 1
        #     if window > counts1:
        #         l += 1
        #         window[s2[l]] -= 1
        #     elif window == counts1:
        #         return True
        # return False