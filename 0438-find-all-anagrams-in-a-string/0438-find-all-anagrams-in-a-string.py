class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # fixed size window
        l = 0
        countS = Counter()
        countP = Counter(p)
        res = []
        for j in range(len(s)):
            countS[s[j]] += 1
            if j-l+1 == len(p):
                if countP == countS:
                    res.append(l)
                countS[s[l]] -= 1
                l += 1
        return res
                
