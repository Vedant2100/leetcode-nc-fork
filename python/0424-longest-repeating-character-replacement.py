class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l, maxf = 0, 0 
        for i in range(len(s)):
            count[s[i]] = 1+ count.get(s[i], 0)
            maxf = max(maxf, count[s[i]])
            if i-l+1 - maxf > k: #more than k substituitions needed
                count[s[l]] -= 1 # slide window
                l += 1
        return i-l+1

