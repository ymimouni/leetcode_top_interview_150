from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        ret = 1

        for i in range(n - 1, -1, -1):
            if digits[i] == 9 and ret == 1:
                digits[i] = 0
            else:
                digits[i] += ret
                return digits

        digits.append(0)
        digits[0] = 1

        return digits
