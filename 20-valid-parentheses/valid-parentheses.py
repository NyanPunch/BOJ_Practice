class Solution:
    def isValid(self, s: str) -> bool:
        if (s[0] == ')' or s[0] == '}' or s[0] == ']'):
            return False
        
        stack = []
        
        for i in s:
            if (i == '(' or i == '{' or i == '['):
                stack.append(i)
            elif (len(stack) != 0) and (stack[-1] == '(' or stack[-1] == '{' or stack[-1] == '['):
                if (i == ')' and stack[-1] == '(') or (i == '}' and stack[-1] == '{') or (i == ']' and stack[-1] == '['):
                    stack.pop()
                else: return False
            else: return False
        if len(stack) == 0: return True
        return False