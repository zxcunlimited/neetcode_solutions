class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        elif s.count(s[0]) == len(s):
            return 1
        char_set = set()
        l = 0
        temp_len = max_len = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
                temp_len -= 1
            temp_len += 1
            char_set.add(s[r])
            if temp_len > max_len:
                max_len = temp_len
        return max_len

