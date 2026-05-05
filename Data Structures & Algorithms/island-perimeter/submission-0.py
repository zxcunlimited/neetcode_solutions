class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def check_neigh(i, j) -> int:
            res = 0
            res += (i - 1 >= 0) and (grid[i - 1][j] == 1)
            res += (i + 1 <= row - 1) and (grid[i + 1][j] == 1)
            res += (j - 1 >= 0) and (grid[i][j - 1] == 1)
            res += (j + 1 <= col - 1) and (grid[i][j + 1] == 1)
            return res
        
        per = 0
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    per += 4 - check_neigh(i, j)
        return per