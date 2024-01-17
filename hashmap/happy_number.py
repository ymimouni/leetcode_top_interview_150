class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(n: int):
            sum_ = 0
            while n > 0:
                n, r = divmod(n, 10)
                sum_ += r ** 2
            return sum_

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = next_num(n)

        return n == 1
