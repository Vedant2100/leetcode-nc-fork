class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # we can alwaydsconstruct a set f every window of three
        l = 0
        res=  0
        charset= set()
        # butthis is better
        for j in range(len(s)):
            while s[j] in charset:
                charset.remove(s[l])
                l += 1
            
            charset.add(s[j])

            if j - l + 1 == 3:
                res += 1
                charset.remove(s[l])
                l += 1

        return res