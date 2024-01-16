from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R, C = len(board), len(board[0])
        ans = [[0] * C for _ in range(R)]

        for r in range(R):
            for c in range(C):
                cell = board[r][c]
                neighbors = 0
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if 0 <= i < R and 0 <= j < C:
                            neighbors += board[i][j]
                neighbors -= cell

                if cell == 1 and (neighbors < 2 or neighbors > 3):
                    ans[r][c] = 0
                elif cell == 0 and neighbors == 3:
                    ans[r][c] = 1
                else:
                    ans[r][c] = cell

        for r in range(R):
            for c in range(C):
                board[r][c] = ans[r][c]
