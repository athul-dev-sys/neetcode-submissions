class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=''.join(c.lower() for c in s if c.isalnum())
        if l==l[::-1]:
            return True
        else:
            return False
        