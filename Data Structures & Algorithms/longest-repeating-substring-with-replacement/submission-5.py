class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        alphabet = dict()
        max_len = 0
        l = 0
        for i in range(len(s)):
            if alphabet.get(s[i], -1) == -1:
                alphabet.update({s[i]: 1})
            else:
                alphabet[s[i]] += 1
            if len(alphabet) > 1:
                replacements = (i - l + 1) - max(alphabet.values())
                while replacements > k:
                    alphabet[s[l]] -= 1
                    l += 1
                    replacements = (i - l + 1) - max(alphabet.values())
            wind_len = i - l + 1
            max_len = max(max_len, wind_len)
        return max_len