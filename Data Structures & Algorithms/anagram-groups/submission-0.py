class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag_grp={}
        for i in strs:
            key = ''.join(sorted(i))
            if key not in anag_grp:
                anag_grp[key]=[]
            anag_grp[key].append(i)
        return list(anag_grp.values())

