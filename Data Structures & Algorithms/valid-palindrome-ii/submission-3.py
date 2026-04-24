class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if s[l + 1:r + 1] == s[r:l:-1] or s[l:r] == s[r - 1:l - 1:-1]:
                    return True
                else:
                    return False