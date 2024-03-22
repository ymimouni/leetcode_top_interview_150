from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row: int, col: int, idx: int) -> bool:
            if idx == len(word) - 1:
                return board[row][col] == word[idx]
            elif board[row][col] != word[idx]:
                return False

            ret = False
            letter = board[row][col]
            board[row][col] = "#"
            for d in directions:
                next_row, next_col = row + d[0], col + d[1]
                if 0 <= next_row < R and 0 <= next_col < C and board[next_row][next_col] != "#":
                    ret = backtrack(next_row, next_col, idx + 1)
                    if ret: break

            board[row][col] = letter

            return ret

        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        R, C = len(board), len(board[0])
        for row in range(R):
            for col in range(C):
                if backtrack(row, col, 0):
                    return True

        return False
