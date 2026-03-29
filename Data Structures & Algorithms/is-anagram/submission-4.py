class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        # if len(s) != len(t):
        #     return False
        # letters1, letters2 = {}, {}
        # for i in range(len(s)):
        #     letters1[s[i]] = 1 + letters1.get(s[i],  0)
        #     letters2[t[i]] = 1 + letters2.get(t[i],  0)
        # return letters1 == letters2