class Solution:
    def climbStairs(self, n: int) -> int:
        
        def fibbonacci(n):
            fibs = [0, 1, 2]
            if n <= 2:
                return fibs[n]
            for i in range(3, n + 1):
                fibs.append(fibs[i - 1] + fibs[i - 2])
            return fibs[-1]

        return fibbonacci(n)