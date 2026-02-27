class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxfreq = 0

        for i in range(len(s)):
            count[s[i]] = 1+ count.get(s[i], 0)
            maxfreq = max(maxfreq, count[s[i]]) #elem with maxfreq
            if i-l+1 -maxfreq > k: # remaining elems are > k then we slide
                count[s[l]] -= 1
                l += 1
            #else: # this s the answer 
                # return i - l + 1     
        return i -l + 1
