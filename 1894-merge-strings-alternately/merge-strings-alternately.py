class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        i = 0
        while True:
            if i >= len(word1) or i >= len(word2):
                break
            result += word1[i]
            result += word2[i]
            i += 1
        if len(word1) > i:
            for n in range(i, len(word1)):
                result += word1[n]
        else:
            for n in range(i, len(word2)):
                result += word2[n]

        return result