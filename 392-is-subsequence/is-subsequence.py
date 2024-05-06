class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0: return True
        i, j = 0, 0
        while i < len(t):
            if t[i] == s[j]:
                j += 1
                if j == len(s): return True
            i += 1
        return False