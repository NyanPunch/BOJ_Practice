class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse_x = str(x)[::-1]
        if str(x) == reverse_x: return True
        return False