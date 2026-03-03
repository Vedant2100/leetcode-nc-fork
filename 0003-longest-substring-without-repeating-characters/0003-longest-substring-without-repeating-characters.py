class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        maxLen = 0
        l = 0
        for j in range(len(s)):
            while s[j] in charset:
                charset.remove(s[l])
                l +=  1
            charset.add(s[j])
            maxLen = max(maxLen, j-l+1)
        return maxLen
        
