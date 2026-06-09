from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        w = {}
        res_len = float('inf')
        res_left = 0
        res_right = 0
        left = 0
        t_count = Counter(t)
        need = len(t_count)
        have = 0
        for right in range(len(s)):
            w[s[right]]=w.get(s[right],0)+1
            if s[right] in t_count and w[s[right]] == t_count[s[right]]:
                have += 1
            while have >= need:
                if right-left+1<res_len:
                    res_left=left
                    res_right=right
                    res_len = right-left+1
                w[s[left]]-=1
                if s[left] in t_count and w[s[left]]<t_count[s[left]]:
                    have-=1
                if w[s[left]]==0:
                    del w[s[left]]
                left+=1
        return s[res_left:res_right+1] if res_len!=float('inf') else ""                
