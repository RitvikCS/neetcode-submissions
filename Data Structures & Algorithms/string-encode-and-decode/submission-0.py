class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = []
        for i in strs:
            enc.append(f"{len(i)}#{i}")
        return "".join(enc)

    def decode(self, s: str) -> List[str]:
        dec = []
        i = 0
        val = ''
        while i<len(s):
            j = i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            i=j+1
            j=i+length
            dec.append(s[i:j])
            i=j

        return dec