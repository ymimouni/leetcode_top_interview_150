from collections import defaultdict, deque
from typing import List


class Solution:
    def __init__(self):
        self.neighbors = defaultdict(list)

    def process_word(self, queue, visited, other_visited):
        l = len(queue)
        for _ in range(l):
            word = queue.popleft()
            for i in range(len(word)):
                for neighbor in self.neighbors[word[:i] + "*" + word[i + 1:]]:
                    if neighbor in other_visited:
                        return visited[word] + other_visited[neighbor]
                    if neighbor not in visited:
                        visited[neighbor] = visited[word] + 1
                        queue.append(neighbor)

        return None

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        for word in wordList:
            for i in range(len(beginWord)):
                self.neighbors[word[:i] + "*" + word[i + 1:]].append(word)

        begin_visited = {beginWord: 1}
        end_visited = {endWord: 1}
        begin_queue = deque([beginWord])
        end_queue = deque([endWord])

        while begin_queue and end_queue:
            if len(begin_queue) <= len(end_queue):
                res = self.process_word(begin_queue, begin_visited, end_visited)
            else:
                res = self.process_word(end_queue, end_visited, begin_visited)

            if res:
                return res

        return 0

    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     neighbors = defaultdict(list)

    #     for word in wordList:
    #         for i in range(len(beginWord)):
    #             neighbors[word[:i] + "*" + word[i + 1:]].append(word)

    #     seen = set()
    #     queue = deque([(beginWord, 1)])

    #     while queue:
    #         word, d = queue.popleft()
    #         if word == endWord:
    #             return d

    #         seen.add(word)

    #         for i in range(len(beginWord)):
    #             for neighbor in neighbors[word[:i] + "*" + word[i + 1:]]:
    #                 if neighbor not in seen:
    #                     queue.append((neighbor, d + 1))

    #     return 0

    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     neighbors = defaultdict(list)

    #     for word in wordList:
    #         for i in range(len(beginWord)):
    #             neighbors[word[:i] + "*" + word[i + 1:]].append(word)

    #     seen = set()

    #     def helper(word: str) -> Optional[int]:
    #         if word == endWord:
    #             return 1

    #         seen.add(word)

    #         min_words = float("inf")

    #         for i in range(len(word)):
    #             for neighbor in neighbors[word[:i] + "*" + word[i + 1:]]:
    #                 if neighbor not in seen:
    #                     res = helper(neighbor)
    #                     if res:
    #                         min_words = min(min_words, res)

    #         seen.remove(word)
    #         return 1 + min_words

    #     min_words = helper(beginWord)

    #     return 0 if min_words is None or min_words == float("inf") else min_words

# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         letters = "abcdefghijklmnopqrstuvwxyz"
#         words = set(wordList)
#         seen = set()
#         min_words = float("inf")

#         def helper(word: str, num_words: int) -> None:
#             nonlocal min_words

#             if word == endWord:
#                 min_words = min(min_words, num_words)
#                 return None

#             seen.add(word)

#             for i in range(len(word)):
#                 for c in letters:
#                     new_word = word[:i] + c + word[i + 1:]
#                     if new_word not in seen and new_word in words:
#                         helper(new_word, num_words + 1)

#             seen.remove(word)

#         helper(beginWord, 1)

#         return 0 if min_words == float("inf") else min_words
