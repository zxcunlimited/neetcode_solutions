class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        задача немного странна описана но суть в том, что должны остаться те регионы, у которых
        ХОТЯ БЫ ОДИН квадрат находится возле края
        самое простое решение - пройти по краю, запустить dfs для тех квадратов которые встретили
        и занести их в посещенные, потом вторым проходом заменить на X тех, которые не попали в множество
        посещенных квадратов
        """

        n, m = len(board), len(board[0])
        safe = set()

        def surround(i, j):
            if 1 <= i < n - 1 and 1 <= j < m - 1:
                return False
            return True

        def dfs(i, j):
            if (i, j) in safe or min(i, j) < 0 or i == n or j == m or board[i][j] == "X":
                return
            safe.add((i, j))
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(n):
            for j in range(m):
                if surround(i, j):
                    dfs(i, j)
        
        for i in range(n):
            for j in range(m):
                if (i, j) not in safe:
                    board[i][j] = "X"