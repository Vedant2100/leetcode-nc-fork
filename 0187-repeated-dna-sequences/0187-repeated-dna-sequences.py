class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        #O(n) to find all 10 letter seuqences 
        l = 0
        count = set()
        res = set()
        seq= ""
        # below is framework for fixes size window , justdo slicing 
        for i in range(len(s) - 9):
            seq = s[i : i + 10] 
            if seq in count:
                res.add(seq)
            else:
                count.add(seq)
        return list(res)
