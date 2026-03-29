class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            for char in word:
                res += chr((ord(char) + 1) % 256)
            res += " "
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        temp = ""
        for char in s:
            if char != " ":
                temp += chr((ord(char) - 1) % 256)
            else:
                res.append(temp)
                temp = ""
        return res