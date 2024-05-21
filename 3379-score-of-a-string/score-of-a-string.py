class Solution:
    def scoreOfString(self, s: str) -> int:
        # ord, abs
        result = 0
        i = 0
        while i < len(s)-1:
            result += abs(ord(s[i]) - ord(s[i+1]))
            i += 1

        return result