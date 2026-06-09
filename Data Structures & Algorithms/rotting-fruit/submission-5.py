class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        мульти bfs решение, наподобие того что было со стенами и сокровищами, но так как нам нужно
        максимальное время, то нашим ответом будет значение distance после окончания работы программы,
        если мы заразили все фрукты, иначе возвращаем -1
        для этого можно банально посчитать все нормальные фрукты во время прохода
        '''
        n, m = len(grid), len(grid[0])
        visited = set()
        queue = []
        self.normal = 0

        def bfs(i, j):
            if min(i, j) < 0 or i == n or j == m or (i, j) in visited or grid[i][j] == 0:
                return
            self.normal -= 1
            visited.add((i, j))
            queue.append([i, j])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append([i, j])
                    visited.add((i, j))
                elif grid[i][j] == 1:
                    self.normal += 1

        if self.normal == 0:
            return 0

        distance = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.pop(0)
                grid[i][j] = 2
                bfs(i - 1, j)
                bfs(i + 1, j)
                bfs(i, j - 1)
                bfs(i, j + 1)
            distance += 1

        return distance - 1 if self.normal == 0 else -1