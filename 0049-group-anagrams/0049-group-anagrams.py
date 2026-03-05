class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = defaultdict(list)
        # for s in strs:
        #     new = "".join(sorted(list(s)))
        #     res[new].append(s)
        # return list(res.values())
        # #O(snlogn)

        # other way since hashmaps cant be keys 
        
        res = collections.defaultdict(list)
        for s in strs:
            countAlpha = [0] * 26 # since only lowercase alphabet
            for c in s:
                countAlpha[ord(c) - ord('a')] += 1
            res[tuple(countAlpha)].append(s)
        return list(res.values())
    