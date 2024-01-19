from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }

        stack = []
        for token in tokens:
            if token in operations:
                operation = operations[token]
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                stack.append(operation(operand_1, operand_2))
            else:
                stack.append(int(token))

        return stack[-1]
