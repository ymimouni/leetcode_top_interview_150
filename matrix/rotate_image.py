from math import ceil
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        R, C = len(matrix), len(matrix[0])

        for r in range(ceil(R / 2)):
            for c in range(C // 2):
                tmp = matrix[r][c]
                matrix[r][c] = matrix[R - c - 1][r]
                matrix[R - c - 1][r] = matrix[R - r - 1][C - c - 1]
                matrix[R - r - 1][C - c - 1] = matrix[c][C - r - 1]
                matrix[c][C - r - 1] = tmp

    # def rotate(self, matrix: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #     R, C = len(matrix), len(matrix[0])

    #     for r in range(R):
    #         for c in range(min(r, C)):
    #             matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    #     for r in range(R):
    #         for c in range(C // 2):
    #             matrix[r][c], matrix[r][C - 1 - c] = matrix[r][C - 1 - c], matrix[r][c]
