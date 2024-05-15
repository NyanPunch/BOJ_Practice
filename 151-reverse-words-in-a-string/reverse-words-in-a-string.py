class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.split(' ')

        l = len(li)
        i = 0
        result = []
        while i < l:
            if li[i] == '':
                i += 1
                continue
            result.append(li[i])
            i += 1
        result.reverse()
        return ' '.join(result)