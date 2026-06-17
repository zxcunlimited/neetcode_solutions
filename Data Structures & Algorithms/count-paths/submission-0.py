class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        grid[0][0] = 1

        def dfs(i, j):
            if grid[i][j] != 0:
                return grid[i][j]
            temp = 0
            if i - 1 >= 0: temp += dfs(i - 1, j)
            if j - 1 >= 0: temp += dfs(i, j - 1)
            grid[i][j] = temp
            return temp

        dfs(m - 1, n - 1)
        return grid[m - 1][n - 1]
