class Solution:
    def longestPalindrome(self, s: str) -> str:
        # брутфорс (да к тому же еще и не проходящий по времени)
        # self.res = ""
        # def recurse(cur):
        #     if cur == cur[::-1]:
        #         self.res = max(self.res, cur, key = len)
        #         return
        #     recurse(cur[:-1])
        #     recurse(cur[1:])
        # recurse(s)
        # return self.res

        # уже получше решение
        res = ""
        res_len = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res_len = (r - l + 1)
                    res = s[l:r + 1]
                l -= 1
                r += 1
            l, r = i - 1, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > res_len:
                    res_len = (r - l + 1)
                    res = s[l:r + 1]
                l -= 1
                r += 1
        return res