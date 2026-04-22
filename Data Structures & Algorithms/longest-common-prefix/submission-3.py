class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs[1:]:
            if s == "":
                return ""
            for i in range(min(len(s), len(prefix))):
                if s[i] != prefix[i]:
                    prefix = prefix[:i]
                    break
            else:
                prefix = min(prefix, s)

        return prefix