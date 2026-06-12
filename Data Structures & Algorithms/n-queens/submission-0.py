class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        self.res = []

        def is_safe(r: int, c: int, board):
            row = r - 1
            while row >= 0:
                if board[row][c] == "Q":
                    return False
                row -= 1

            row, col = r - 1, c - 1
            while row >= 0 and col >= 0:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col -= 1

            row, col = r - 1, c + 1
            while row >= 0 and col < len(board):
                if board[row][col] == "Q":
                    return False
                row -= 1
                col += 1
            return True

        def backtrack(remaining, board):
            if remaining == n:
                temp = []
                for elem in board:
                    temp.append("".join(elem))
                self.res.append(temp)
                return 1
            for col in range(n):
                if is_safe(remaining, col, board):
                    board[remaining][col] = "Q"
                    backtrack(remaining + 1, board)
                    board[remaining][col] = "."

        backtrack(0, [["." for _ in range(n)] for _ in range(n)])
        return self.res