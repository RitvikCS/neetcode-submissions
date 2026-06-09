class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        s1_dict = {}
        w_freq = {}
        for i in range(len(s1)):
            s1_dict[s1[i]]=s1_dict.get(s1[i],0)+1
            w_freq[s2[i]]=w_freq.get(s2[i],0)+1
        if s1_dict == w_freq:
            return True
        
        for i in range(len(s1),len(s2)):
            w_freq[s2[i]]=w_freq.get(s2[i],0)+1
            left_char = i-len(s1)
            w_freq[s2[left_char]]=w_freq.get(s2[left_char],0)-1
            if w_freq[s2[left_char]]==0:
                del w_freq[s2[left_char]]
            if s1_dict == w_freq:
                return True

        return False