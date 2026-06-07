class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.n, self.m = len(grid), len(grid[0])
        def corrupt(x, y):
            if grid[y][x] == 1:
                self.cur_area += 1
                grid[y][x] = 0
            else:
                return
            l_x, r_x = x - 1, x + 1
            u_y, d_y = y - 1, y + 1
            if l_x >= 0: corrupt(l_x, y)
            if r_x < self.m: corrupt(r_x, y)
            if u_y >= 0: corrupt(x, u_y)
            if d_y < self.n: corrupt(x, d_y)
        res = 0
        self.cur_area = 0
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 1:
                    self.cur_area = 0
                    corrupt(j, i)
                    res = max(res, self.cur_area)
        return res
