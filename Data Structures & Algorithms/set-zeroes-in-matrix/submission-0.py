class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        zero_idx = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0: zero_idx.append((i, j)) 
        while zero_idx != []:
            cur = zero_idx.pop()
            cur_i, cur_j = cur[0], cur[1]
            for j in range(m):
                matrix[cur_i][j] = 0
            for i in range(n):
                matrix[i][cur_j] = 0
                