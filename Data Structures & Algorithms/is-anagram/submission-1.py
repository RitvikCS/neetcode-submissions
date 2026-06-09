class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check_s = {}
        check_t = {}
        if len(s) != len(t):
            return False
        for i in s:
            check_s[i] = check_s.get(i, 0) + 1
        for i in t:
            check_t[i] = check_t.get(i, 0) + 1
        print(check_s)
        print(check_t)
        if check_s == check_t:
            return True
        else:
            return False
