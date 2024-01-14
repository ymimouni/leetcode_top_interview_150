from typing import List


class Solution:
    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        ans = []
        line_length = last_idx = 0
        current_length = 0

        for word in words:
            if current_length + line_length + len(word) > max_width:
                full_line = []
                spaces = max_width - current_length
                # use max with 1 to avoid division and modulo by 0
                q, r = spaces // max(1, (line_length - 1)), spaces % max(1, (line_length - 1))
                for i in range(last_idx, last_idx + line_length):
                    full_line.append(words[i])
                    full_line.append(' ' * (q + (1 if r else 0)))
                    r = max(0, r - 1)
                if line_length > 1:
                    full_line.pop()

                ans.append(''.join(full_line))
                last_idx += line_length
                line_length = 0
                current_length = 0

            line_length += 1
            current_length += len(word)

        ans.append(' '.join(words[last_idx:]).ljust(max_width, ' '))

        return ans
