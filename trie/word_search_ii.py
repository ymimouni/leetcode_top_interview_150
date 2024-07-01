from collections import defaultdict
from typing import DefaultDict, List


class Dictionary:
    WORD_END = "#"

    def __init__(self, dictionary: List[str] = None):
        self.trie = Dictionary.r_ddict()
        for word in dictionary:
            self.insert(word)

    def r_ddict() -> DefaultDict:
        return defaultdict(Dictionary.r_ddict)

    def insert(self, word: str) -> None:
        node = self.trie
        for c in word:
            node = node[c]
        node[Dictionary.WORD_END] = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def helper(parent: DefaultDict, row: int, col: int) -> None:
            c = board[row][col]
            if c not in parent:
                return None
            board[row][col] = '$'
            node = parent[c]

            word_match = node.pop(Dictionary.WORD_END, False)
            if word_match:
                ans.append(word_match)

            for d in directions:
                next_row, next_col = row + d[0], col + d[1]
                if (
                    0 <= next_row < R
                    and 0 <= next_col < C
                    and board[next_row][next_col] != '$'
                ):
                    helper(node, next_row, next_col)

            board[row][col] = c
            if not node:
                parent.pop(c)

        dictionary = Dictionary(words).trie
        ans = []

        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        R, C = len(board), len(board[0])
        for row in range(R):
            for col in range(C):
                helper(dictionary, row, col)

        return ans
