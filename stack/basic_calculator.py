from typing import List


class Solution:
    def evaluate_expression(self, stack: List[int | str]) -> int:
        if stack[-1] == '-':
            stack.append(0)

        res = stack.pop()
        while stack and stack[-1] != ')':
            operation, operand_2 = stack.pop(), stack.pop()
            if operation == '+':
                res += operand_2
            elif operation == '-':
                res -= operand_2

        return res

    def calculate(self, s: str) -> int:
        stack = []

        n = operand = 0
        for i in range(len(s) - 1, -1, -1):
            c = s[i]

            if c.isdigit():
                operand += int(c) * 10 ** n
                n += 1
            elif not c.isspace():
                if n != 0:
                    stack.append(operand)
                    n = operand = 0

                if c == '(':
                    res = self.evaluate_expression(stack)
                    stack.pop()
                    stack.append(res)
                else:
                    stack.append(c)

        if n != 0:
            stack.append(operand)

        return self.evaluate_expression(stack)
