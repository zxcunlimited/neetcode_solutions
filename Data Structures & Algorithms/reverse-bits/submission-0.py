class Solution:
    def reverseBits(self, n: int) -> int:
        # return int(bin(n)[2:][::-1], 2)
        num = bin(n)[2:][::-1]
        return int(num + "0" * (32 - len(num)), 2)