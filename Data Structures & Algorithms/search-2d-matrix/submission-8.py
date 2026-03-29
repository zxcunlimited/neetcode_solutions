class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # интуитивное решение с созданием новой матрицы, примерная сложность
        # O(m * n + log(m * n))
        # full = []
        # for i in range(len(matrix)):
        #     full.extend(matrix[i])
        # n = len(full)
        # l, r = 0, n
        # while l < r:
        #     mid = (l + r) // 2
        #     if full[mid] == target:
        #         return True
        #     elif full[mid] > target:
        #         r = mid - 1
        #     else:
        #         l = mid + 1
        # try:
        #     if full[(l + r) // 2] == target:
        #         return True
        #     else:
        #         return False
        # except IndexError:
        #     return False

        # нормальное решение с линейным индексированием по массиву
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid // n][mid % n] == target:
                return True
            elif matrix[mid // n][mid % n] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False