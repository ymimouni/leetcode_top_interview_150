class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 0, x // 2
        while left <= right:
            pivot = (left + right) // 2
            square = pivot * pivot
            if square < x:
                left = pivot + 1
            elif square > x:
                right = pivot - 1
            else:
                return pivot

        return right

    # def mySqrt(self, x: int) -> int:
    #     if x < 2:
    #         return x

    #     for k in range(0, x // 2 + 1):
    #         if k * k > x:
    #             break

    #     left, right = k - 1, k

    #     return left if right * right > x else right
