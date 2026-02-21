class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        
        countT = Counter(t)
        window = Counter()
        
        l = 0
        minLen = float('inf')
        res = ''
        
        for r in range(len(s)):
            window[s[r]] += 1   # expand right
            
            # shrink while valid
            while window >= countT:
                if (r - l + 1) < minLen:
                    minLen = r - l + 1
                    res = s[l:r+1]
                
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
        
        return res