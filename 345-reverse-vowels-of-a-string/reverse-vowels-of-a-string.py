class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        li1 = []
        li2 = []
        for i in range(len(s)):
            if s[i] in vowels:
                li1.append(i)   # li1 = [1, 4]
                li2.append(s[i])# li2 = ['e', 'o'] 
        
        for j in range(len(li1)):
            s = s[:li1[j]] + li2[-j-1] + s[li1[j]+1:]
        return s
    