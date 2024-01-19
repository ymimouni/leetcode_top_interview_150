class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_ = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in map_:
                if not stack or stack[-1] != map_[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return not stack
