from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        seen = set()

        # Rows
        for r in range(N):
            for c in range(N):
                cell = board[r][c]
                if cell != '.' and cell in seen:
                    return False
                seen.add(cell)
            seen = set()

        # Columns
        for c in range(N):
            for r in range(N):
                cell = board[r][c]
                if cell != '.' and cell in seen:
                    return False
                seen.add(cell)
            seen = set()

        # Boxes.
        for r_offset in range(0, 9, 3):
            for c_offset in range(0, 9, 3):
                for r in range(3):
                    for c in range(3):
                        cell = board[r_offset + r][c_offset + c]
                        if cell != '.' and cell in seen:
                            return False
                        seen.add(cell)
                seen = set()

        return True
