class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        """
        идея оптимизации следующая - мы идем от обратного. вместо того чтобы каждой клетке
        считать может ли она дойти до границы одного из океанов, мы начинаем с самих границ
        и представляем себя океаном - если мы можем дойти до клетки, значит и клетка может дойти
        до нас. в таком случае решение облегается до нахождения того, до каких клеток могут дойти
        океаны и потом просто выполнить пересечение множеств.
        """

        pac, atl = set(), set()
        n, m = len(heights), len(heights[0])

        def dfs(i, j, cur, visited):
            if (i, j) in visited:
                return

            cur.add((i, j))
            visited.add((i, j))
            if i - 1 >= 0:
                if heights[i - 1][j] >= heights[i][j]: dfs(i - 1, j, cur, visited)
            if i + 1 < n:
                if heights[i + 1][j] >= heights[i][j]: dfs(i + 1, j, cur, visited)
            if j - 1 >= 0:
                if heights[i][j - 1] >= heights[i][j]: dfs(i, j - 1, cur, visited)
            if j + 1 < m:
                if heights[i][j + 1] >= heights[i][j]: dfs(i, j + 1, cur, visited)

        for j in range(m):
            dfs(0, j, pac, set())
            dfs(n - 1, j, atl, set())
        for i in range(n):
            dfs(i, 0, pac, set())
            dfs(i, m - 1, atl, set())

        res = []
        for i in range(n):
            for j in range(m):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])

        return res