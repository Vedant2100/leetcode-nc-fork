class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window new charcomes trim left
        charset = set()
        l = 0
        res = 0

        # one pass way  
        for i in range(len(s)):
            while s[i] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[i])
            res = max(res, i - l + 1)
        
        return res
