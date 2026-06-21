class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        i = 0
        for elem in digits[::-1]:
            num += (10 ** i) * elem
            i += 1
        num += 1
        return [int(i) for i in str(num)]