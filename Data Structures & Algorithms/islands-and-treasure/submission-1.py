class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # обычное BFS решение
        # self.m, self.n = len(grid[0]), len(grid)
        # def traverse(i, j, steps):
        #     if grid[i][j] == -1 or grid[i][j] < steps:
        #         return
        #     grid[i][j] = min(grid[i][j], steps)
        #     left = j - 1
        #     right = j + 1
        #     up = i - 1
        #     down = i + 1
        #     if 0 <= left: traverse(i, left, steps + 1)
        #     if right < self.m: traverse(i, right, steps + 1)
        #     if 0 <= up: traverse(up, j, steps + 1)
        #     if down < self.n: traverse(down, j, steps + 1)
        
        # for y in range(self.n):
        #     for x in range(self.m):
        #         if grid[y][x] == 0:
        #             traverse(y, x, 0)

        """ 
        мульти BFS решение - запуск одновременно из каждого 'сокровища'
        при запуске от каждого сокровища, нам не нужно просчитывать минимум из шагов и того, какое
        количество шагов уже было, потому что если мы дошли до текущей клетки и она не была
        посещена - то минимальное расстояние и есть то число шагов которые мы потратили
        в таком случае появляются новые составляющие решения:
        - множество посещенных клеток для того чтобы правильно использовать данное решение
        - функция bfs меняется и теперь использует очередь, которая составляется следующим образом:
        - - при первом (и единственном) проходе по всему полю каждое сокровище добавляется в список
        - - потом, пока очередь существует мы достаем из нее элемент и запускаем для него bfs. в bfs
        клетка проверяется на соответствие границам и присутствию в списке уже посещенных клеток,
        если все нормально, то для текущей клетки устанавливаем расстояние и добавляем соседей в 
        очередь, запуская таким образом для них bfs 
        благодаря этому уменьшается временная сложность с O((m * n) ^ 2) (каждая клетка могла
        проверяться каждый раз если до нее доходили из какого-либо сокровища) до O((m * n))
        """
        m, n = len(grid[0]), len(grid)
        queue = []
        visited = set()

        def bfs(i, j):
            if i >= n or i < 0 or j >= m or j < 0 or (i, j) in visited or grid[i][j] == -1:
                return
            visited.add(tuple([i, j]))
            queue.append([i, j])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    queue.append([i, j])
                    visited.add(tuple([i, j]))

        distance = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.pop(0)
                grid[i][j]  = distance
                bfs(i - 1, j)
                bfs(i + 1, j)
                bfs(i, j - 1)
                bfs(i, j + 1)
            distance += 1
