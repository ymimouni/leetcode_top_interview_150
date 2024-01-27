from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        visited = set()
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        def dfs(row: int, col: int) -> None:
            if (row, col) in visited:
                return None

            visited.add((row, col))

            for d in directions:
                new_row, new_col = row + d[0], col + d[1]
                if 0 <= new_row < m and 0 <= new_col < n and board[new_row][new_col] == 'O':
                    dfs(new_row, new_col)

        for r in range(m):
            for c in (0, n - 1):
                if board[r][c] == 'O':
                    dfs(r, c)

        for c in range(n):
            for r in (0, m - 1):
                if board[r][c] == 'O':
                    dfs(r, c)

        for r in range(m):
            for c in range(n):
                if (r, c) not in visited and board[r][c] == 'O':
                    board[r][c] = 'X'

        return None
