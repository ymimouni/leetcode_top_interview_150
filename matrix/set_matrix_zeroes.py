from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R, C = len(matrix), len(matrix[0])
        is_col = False

        for r in range(R):
            if matrix[r][0] == 0:
                is_col = True
            for c in range(1, C):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for c in range(1, C):
            if matrix[0][c] == 0:
                for r in range(R):
                    matrix[r][c] = 0

        for r in range(R):
            if matrix[r][0] == 0:
                for c in range(C):
                    matrix[r][c] = 0

        if is_col:
            for r in range(R):
                matrix[r][0] = 0
