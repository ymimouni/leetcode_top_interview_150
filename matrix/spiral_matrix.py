from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        R, C = len(matrix), len(matrix[0])
        ans = []

        offset = 0
        while len(ans) < R * C:
            # Move right.
            for c in range(offset, C - offset):
                ans.append(matrix[offset][c])

            # Move down.
            for r in range(offset + 1, R - offset):
                ans.append(matrix[r][C - offset - 1])

            # Move left.
            if R - offset - 1 != offset:
                for c in range(C - offset - 2, offset - 1, -1):
                    ans.append(matrix[R - offset - 1][c])

            # Move right.
            if offset != C - offset - 1:
                for r in range(R - offset - 2, offset, -1):
                    ans.append(matrix[r][offset])

            offset += 1

        return ans
