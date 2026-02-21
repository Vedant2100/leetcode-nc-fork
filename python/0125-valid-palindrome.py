class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = ''
        for a in s:
            if a.isalnum():
                c += a.lower()
        return c == c[::-1]