class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n:
            temp = sum([int(i) ** 2 for i in str(n)])
            if temp in seen:
                return False
            if temp == 1:
                return True
            seen.add(temp)
            n = temp