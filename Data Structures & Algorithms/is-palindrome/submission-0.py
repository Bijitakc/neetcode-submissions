class Solution:
    def isPalindrome(self, s: str) -> bool:
        l_s = ''.join(c.lower() for c in s if c.isalnum())
        left = 0
        right = len(l_s) - 1

        while (left <= right):
            if l_s[left] != l_s[right]:
                return False
            left += 1
            right -= 1
        return True
