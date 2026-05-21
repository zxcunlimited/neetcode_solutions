class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.n, self.m = len(board), len(board[0])
        self.res = False
        def graph(cur, board, i, j, completed):
            if self.res == True:
                return
            if cur == word:
                self.res = True
                return
            if len(cur) == len(word):
                return
            low_i, up_i = i + 1 if (i + 1) < self.n else -1, i - 1 if (i - 1) > -1 else -1
            left_j, right_j = j + 1 if (j + 1) < self.m else -1, j - 1 if (j - 1) > -1 else -1
            if low_i != -1 and (low_i, j) not in completed: graph(cur + board[low_i][j], board, low_i, j, completed + [(i, j)])
            if up_i != -1 and (up_i, j) not in completed: graph(cur + board[up_i][j], board, up_i, j, completed + [(i, j)])
            if left_j != -1 and (i, left_j) not in completed: graph(cur + board[i][left_j], board, i, left_j, completed + [(i, j)])
            if right_j != -1 and (i, right_j) not in completed: graph(cur + board[i][right_j], board, i, right_j, completed + [(i, j)])
        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] == word[0]:
                    graph(board[i][j], board, i, j, [(i, j)])
                    if self.res:
                        return True
        return False