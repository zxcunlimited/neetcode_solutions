class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        count = 0
        box_n = -1
        nums = set([str(num) for num in range(1, 10)])
        box = [set() for i in range(3)]
        cols = [set() for i in range(9)]
        for i in range(9):
            if i % 3 == 0:
                box = [set() for i in range(3)]
            row = set()
            for j in range(9):
                count += 1
                if count % 3 == 1:
                    box_n = (box_n + 1) % 3
                if board[i][j] != ".":
                    if board[i][j] in box[box_n] or board[i][j] not in nums:
                        return False
                    box[box_n].add(board[i][j])
                    if board[i][j] in row or board[i][j] not in nums:
                        return False
                    row.add(board[i][j])
                    if board[i][j] in cols[j] or board[i][j] not in nums:
                        return False
                    cols[j].add(board[i][j])
        return True