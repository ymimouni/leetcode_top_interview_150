from collections import defaultdict
from typing import DefaultDict


class WordDictionary:
    def __init__(self):
        self.trie = WordDictionary.r_ddict()

    def r_ddict() -> defaultdict:
        return defaultdict(WordDictionary.r_ddict)

    def addWord(self, word: str) -> None:
        node = self.trie

        for c in word:
            node = node[c]

        node['#'] = True

    def search(self, word: str) -> bool:
        def helper(node: DefaultDict, start: int) -> bool:
            for i in range(start, len(word)):
                c = word[i]
                if c == '.':
                    for k, v in node.items():
                        if k != '#' and helper(v, i + 1):
                            return True
                    return False
                elif c not in node:
                    return False
                else:
                    node = node[c]
            return '#' in node
        node = self.trie
        return helper(node, 0)
