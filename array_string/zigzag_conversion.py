class Solution:
    def matrix_gen(self, matrix):
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                yield matrix[row][col]

    # def convert(self, s: str, num_rows: int) -> str:
    #     if num_rows == 1:
    #         return s

    #     n = len(s)
    #     num_cols = ceil(n / (2 * num_rows - 2)) * (num_rows - 1)
    #     matrix = [[''] * num_cols for _ in range(num_rows)]

    #     row, col = 0, 0
    #     index = 0

    #     while index < n:
    #         while row < num_rows and index < n:
    #             matrix[row][col] = s[index]
    #             index += 1
    #             row += 1

    #         row -= 2
    #         col += 1

    #         while index < n and row > 0:
    #             matrix[row][col] = s[index]
    #             row -= 1
    #             col += 1
    #             index += 1

    #     return ''.join(self.matrix_gen(matrix))

    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s

        n = len(s)
        num_cells_per_sec = 2 * num_rows - 2
        index = 0
        answer = []

        for row in range(num_rows):
            index = row
            while index < n:
                answer.append(s[index])

                if row != 0 and row != num_rows - 1:
                    second_index = index + num_cells_per_sec - 2 * row
                    if second_index < n:
                        answer.append(s[second_index])

                index += num_cells_per_sec

        return ''.join(answer)
