class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row: int) -> None:
            nonlocal ans

            if row == n:
                ans += 1
                return None

            for col in range(n):
                diagonal = row - col
                anti_diagonal = row + col
                if col in cols or diagonal in diagonals or anti_diagonal in anti_diagonals:
                    continue
                cols.add(col)
                diagonals.add(diagonal)
                anti_diagonals.add(anti_diagonal)
                backtrack(row + 1)
                cols.remove(col)
                diagonals.remove(diagonal)
                anti_diagonals.remove(anti_diagonal)

            return None

        ans = 0
        cols, diagonals, anti_diagonals = set(), set(), set()
        backtrack(0)
        return ans
