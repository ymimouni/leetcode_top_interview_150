from collections import defaultdict


class Trie:
    def __init__(self):
        self.trie = Trie.r_ddict()

    @staticmethod
    def r_ddict():
        return defaultdict(Trie.r_ddict)

    def insert(self, word: str) -> None:
        cur = self.trie
        for c in word:
            cur = cur[c]
        cur['#'] = True

    def search(self, word: str) -> bool:
        cur = self.trie
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return '#' in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.trie
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True
