class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for portion in path.split('/'):
            # If the current portion is a "..", then we pop an entry from the stack
            # if it's not empty.
            if portion == "..":
                if stack:
                    stack.pop()
            elif not portion or portion == '.':
                # A no-op for an empty portion or a '.'.
                continue
            else:
                # A legitimate directory name, add it to the stack.
                stack.append(portion)

        # Stitch together the directory names.
        result = '/' + '/'.join(stack)
        return result
