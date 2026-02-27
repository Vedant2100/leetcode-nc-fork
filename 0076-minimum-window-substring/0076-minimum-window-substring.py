class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = collections.Counter(t)
        window = collections.Counter()
        l = 0
        res = ""
        minLen = float('inf')

        for r in range(len(s)):
            window[s[r]] += 1
            while countT <= window:
                if (r - l + 1) < minLen:
                    minLen = r - l + 1
                    res = s[l : r + 1]              
                window[s[l]] -= 1
                l += 1
                
        return res