class Solution:
    def tribonacci(self, n: int) -> int:
        tribs = [0, 1, 1]
        for i in range(2, n):
            tribs.append(tribs[i] + tribs[i - 1] + tribs[i - 2])
        return tribs[n]