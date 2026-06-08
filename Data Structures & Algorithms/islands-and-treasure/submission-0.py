class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.m, self.n = len(grid[0]), len(grid)
        def traverse(i, j, steps):
            if grid[i][j] == -1 or grid[i][j] < steps:
                return
            grid[i][j] = min(grid[i][j], steps)
            left = j - 1
            right = j + 1
            up = i - 1
            down = i + 1
            if 0 <= left: traverse(i, left, steps + 1)
            if right < self.m: traverse(i, right, steps + 1)
            if 0 <= up: traverse(up, j, steps + 1)
            if down < self.n: traverse(down, j, steps + 1)
        
        for y in range(self.n):
            for x in range(self.m):
                if grid[y][x] == 0:
                    traverse(y, x, 0)